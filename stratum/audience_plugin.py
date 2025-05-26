"""
Stratum Audience Plugin - Material Design Compatible
Clean audience targeting with Material theme integration.
"""

import re
import html
import logging
import yaml
from typing import Dict, List, Set, Tuple
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page
from mkdocs.structure.files import File, Files

logger = logging.getLogger(__name__)

class StratumAudienceConfig(config_options.Config):
    audiences = config_options.Type((list, str), default=['internal', 'partner', 'beta'])
    default_audience = config_options.Type(str, default='public')
    comment_start = config_options.Type(str, default='<!-- audience:')
    comment_end = config_options.Type(str, default='-->')
    comment_close = config_options.Type(str, default='<!-- /audience -->')
    auto_labels = config_options.Type(bool, default=True)
    label_style = config_options.Choice(['badge', 'text', 'none'], default='badge')
    sanitize_html = config_options.Type(bool, default=True)
    debug = config_options.Type(bool, default=False)

class StratumAudiencePlugin(BasePlugin[StratumAudienceConfig]):
    def __init__(self):
        super().__init__()
        self.current_audiences: Set[str] = set()
        self.page_audiences: Dict[str, Set[str]] = {}
        
    def on_config(self, config, **kwargs):
        # Normalize audiences configuration
        if isinstance(self.config.audiences, str):
            self.config.audiences = [aud.strip() for aud in self.config.audiences.split(',')]
            
        if self.config.debug:
            logger.setLevel(logging.DEBUG)
            logger.debug(f"Stratum initialized with audiences: {self.config.audiences}")
            
        # Get current build audience
        extra = config.get('extra', {})
        self.current_audiences = set()
        
        if extra.get('audience_internal', False):
            self.current_audiences.add('internal')
        if extra.get('audience_partner', False):
            self.current_audiences.add('partner')  
        if extra.get('audience_beta', False):
            self.current_audiences.add('beta')
            
        if not self.current_audiences:
            self.current_audiences.add('public')
            
        if self.config.debug:
            logger.debug(f"Current build audiences: {self.current_audiences}")
            
        return config
    
    def on_files(self, files: Files, config, **kwargs) -> Files:
        """Filter pages based on audience targeting."""
        filtered_files = Files([])
        
        for file in files:
            if file.src_path.endswith('.md'):
                page_audiences = self._get_page_audiences_from_file(file.abs_src_path)
                if self.should_render_page(page_audiences):
                    filtered_files.append(file)
                elif self.config.debug:
                    logger.debug(f"Excluding page: {file.src_path}")
            else:
                filtered_files.append(file)
        
        return filtered_files
    
    def _get_page_audiences_from_file(self, file_path: str) -> Set[str]:
        """Extract audiences from frontmatter."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.startswith('---'):
                return set()
            
            parts = content.split('---', 2)
            if len(parts) < 3:
                return set()
            
            frontmatter = yaml.safe_load(parts[1])
            if not frontmatter:
                return set()
                
            audiences_raw = frontmatter.get('audiences')
            if not audiences_raw:
                return set()
            
            if isinstance(audiences_raw, str):
                return set(aud.strip().lower() for aud in audiences_raw.split(','))
            elif isinstance(audiences_raw, list):
                return set(aud.lower() for aud in audiences_raw)
                
        except Exception as e:
            if self.config.debug:
                logger.warning(f"Could not parse frontmatter from {file_path}: {e}")
        
        return set()
    
    def on_page_markdown(self, markdown: str, page: Page, config, files: Files, **kwargs) -> str:
        """Process audience comments with Material theme compatibility."""
        if self.config.debug:
            logger.debug(f"Processing page: {page.file.src_path}")
            
        return self._process_audience_comments(markdown)
    
    def _process_audience_comments(self, markdown: str) -> str:
        """Transform audience comments to Material-compatible HTML."""
        # Block pattern
        block_pattern = re.compile(
            rf'{re.escape(self.config.comment_start)}\s*([^{re.escape(self.config.comment_end)}]+){re.escape(self.config.comment_end)}'
            rf'(.*?)'
            rf'{re.escape(self.config.comment_close)}',
            re.DOTALL | re.IGNORECASE
        )
        
        def replace_block_comment(match):
            audience_spec = match.group(1).strip()
            content = match.group(2).strip()
            
            included_audiences, excluded_audiences = self._parse_audience_spec(audience_spec)
            
            if not self._should_show_content(included_audiences, excluded_audiences):
                return ""
                
            return self._generate_audience_html(included_audiences, content, 'block')
        
        processed = block_pattern.sub(replace_block_comment, markdown)
        
        # Inline pattern
        inline_pattern = re.compile(
            rf'(^|\s){re.escape(self.config.comment_start)}\s*([^{re.escape(self.config.comment_end)}]+){re.escape(self.config.comment_end)}'
            rf'([^<]*?)'
            rf'{re.escape(self.config.comment_close)}',
            re.IGNORECASE
        )
        
        def replace_inline_comment(match):
            leading_space = match.group(1)
            audience_spec = match.group(2).strip()
            content = match.group(3).strip()
            
            included_audiences, excluded_audiences = self._parse_audience_spec(audience_spec)
            
            if not self._should_show_content(included_audiences, excluded_audiences):
                return leading_space
                
            return leading_space + self._generate_audience_html(included_audiences, content, 'inline')
        
        processed = inline_pattern.sub(replace_inline_comment, processed)
        return processed
    
    def _parse_audience_spec(self, spec: str) -> Tuple[List[str], List[str]]:
        """Parse audience spec with negation support."""
        included_audiences = []
        excluded_audiences = []
        
        for aud in spec.split(','):
            aud = aud.strip().lower()
            
            if aud.startswith('!'):
                excluded_aud = aud[1:].strip()
                if excluded_aud in self.config.audiences or excluded_aud == 'public':
                    excluded_audiences.append(excluded_aud)
            else:
                if aud in self.config.audiences or aud == 'public':
                    included_audiences.append(aud)
                
        return included_audiences, excluded_audiences
    
    def _should_show_content(self, included_audiences: List[str], excluded_audiences: List[str]) -> bool:
        """Determine content visibility."""
        # Check exclusions first
        if excluded_audiences:
            for excluded in excluded_audiences:
                if excluded in self.current_audiences:
                    return False
        
        # Internal sees everything (unless explicitly excluded)
        if 'internal' in self.current_audiences:
            return True
        
        # Check inclusions
        if included_audiences:
            return any(aud in self.current_audiences for aud in included_audiences)
        
        # Default to public visibility
        return 'public' in self.current_audiences
    
    def _generate_audience_html(self, audiences: List[str], content: str, level: str) -> str:
        """Generate Material-compatible HTML with audience classes."""
        if self.config.sanitize_html and level == 'inline':
            safe_content = html.escape(content)
        else:
            safe_content = content
        
        primary_audience = audiences[0] if audiences else 'public'
        
        classes = [f"audience-{primary_audience}", f"stratum-{level}"]
        for aud in audiences:
            audience_class = f"audience-{aud}"
            if audience_class not in classes:
                classes.append(audience_class)
        
        class_attr = ' '.join(classes)
        data_audience = ', '.join(audiences)
        
        label_html = ""
        if self.config.auto_labels and self.config.label_style == 'badge':
            label_html = f'<span class="audience-badge audience-badge--{primary_audience}">{primary_audience.title()}</span> '
        
        if level == 'inline':
            return f'<span class="{class_attr}" data-audience="{data_audience}">{label_html}{safe_content}</span>'
        else:
            return f'<div class="{class_attr}" data-audience="{data_audience}" markdown="1">\n{label_html}\n{safe_content}\n</div>'
    
    def should_render_page(self, page_audiences: Set[str]) -> bool:
        """Check if page should be rendered."""
        if 'internal' in self.current_audiences:
            return True
            
        if not page_audiences:
            return 'public' in self.current_audiences
            
        return bool(page_audiences.intersection(self.current_audiences))

def get_plugin():
    return StratumAudiencePlugin()