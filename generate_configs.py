#!/usr/bin/env python3
"""
Stratum Config Generator
Generates audience-specific MkDocs configurations.
Preserves internal navigation to allow manual additions.
"""

import yaml
import sys
from pathlib import Path
from typing import Dict, Any, Optional

def load_base_config(config_path: Path = None) -> Dict[str, Any]:
    """Load the base mkdocs.yml configuration."""
    if config_path is None:
        config_path = Path("mkdocs.yml")
    
    if not config_path.exists():
        print(f"Error: {config_path} not found")
        print("Please run this script from your project root directory")
        sys.exit(1)
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        return config
    except yaml.YAMLError as e:
        print(f"Error parsing {config_path}: {e}")
        sys.exit(1)

def load_existing_config(config_path: Path) -> Optional[Dict[str, Any]]:
    """Load existing configuration if it exists."""
    if not config_path.exists():
        return None
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Warning: Could not parse existing {config_path}: {e}")
        return None

def create_audience_config(base_config: Dict[str, Any], audience: str, preserve_nav: bool = False, site_name_suffix: str = None) -> Dict[str, Any]:
    """Create audience-specific configuration."""
    
    # Load existing config if we need to preserve nav
    existing_config = None
    if preserve_nav:
        config_path = Path(f"mkdocs.{audience}.yml")
        existing_config = load_existing_config(config_path)
    
    # Start with a copy of base config
    config = base_config.copy()
    
    # Update site name if suffix provided
    if site_name_suffix:
        original_name = config.get('site_name', 'Documentation')
        config['site_name'] = f"{original_name}{site_name_suffix}"
    
    # Set audience in extra section
    if 'extra' not in config:
        config['extra'] = {}
    
    # Set the target audience
    config['extra']['audience'] = audience
    
    # Preserve navigation for specified audiences
    if preserve_nav and existing_config and 'nav' in existing_config:
        print(f"  → Preserving existing navigation for {audience}")
        config['nav'] = existing_config['nav']
    
    return config

def write_config(config: Dict[str, Any], filename: str) -> None:
    """Write configuration to file with proper formatting."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # Custom YAML dump for better formatting
            yaml.dump(config, f, 
                     default_flow_style=False, 
                     allow_unicode=True, 
                     sort_keys=False,
                     indent=2)
        print(f"  ✓ Generated {filename}")
    except Exception as e:
        print(f"  ✗ Error writing {filename}: {e}")

def main():
    """Generate audience-specific MkDocs configurations."""
    
    print("Stratum Config Generator")
    print("=" * 40)
    
    # Load base configuration
    print("Loading base configuration...")
    base_config = load_base_config()
    
    # Check if advanced audiences are enabled
    enable_advanced = False
    plugin_config = base_config.get('plugins', [])
    for plugin in plugin_config:
        if isinstance(plugin, dict) and 'stratum-audience' in plugin:
            audiences_list = plugin['stratum-audience'].get('audiences', [])
            if 'partner' in audiences_list or 'beta' in audiences_list:
                enable_advanced = True
                break
    
    # Define default audiences
    default_audiences = {
        'public': {
            'preserve_nav': False,
            'site_name_suffix': None,  # Keep original site name
            'description': 'Public documentation (default content)'
        },
        'internal': {
            'preserve_nav': True,  # Don't copy nav for internal
            'site_name_suffix': None,  # Keep original site name
            'description': 'Internal documentation (everything + internal content)'
        }
    }
    
    # Define advanced audiences (only when enabled)
    advanced_audiences = {
        'partner': {
            'preserve_nav': False,
            'site_name_suffix': ' - Partner Portal',
            'description': 'Partner documentation (partner content only)'
        },
        'beta': {
            'preserve_nav': False,
            'site_name_suffix': ' - Beta',
            'description': 'Beta documentation (beta content only)'
        }
    }
    
    # Select which audiences to generate
    if enable_advanced:
        audiences = {**default_audiences, **advanced_audiences}
        print("Advanced audience mode detected - generating all configs")
    else:
        audiences = default_audiences
        print("Simple workflow - generating internal/public configs only")
    
    print(f"Generating configurations for {len(audiences)} audiences...\n")
    
    # Generate each audience configuration
    success_count = 0
    for audience, settings in audiences.items():
        print(f"Generating {audience} configuration:")
        print(f"  → {settings['description']}")
        
        if settings['preserve_nav']:
            print(f"  → Preserving existing navigation")
        
        try:
            config = create_audience_config(
                base_config, 
                audience, 
                preserve_nav=settings['preserve_nav'],
                site_name_suffix=settings['site_name_suffix']
            )
            filename = f"mkdocs.{audience}.yml"
            write_config(config, filename)
            success_count += 1
            print()
        except Exception as e:
            print(f"  ✗ Error generating {audience} config: {e}\n")
    
    # Summary
    print("=" * 40)
    print(f"Generated {success_count}/{len(audiences)} configurations successfully")
    
    if success_count > 0:
        print("\nUsage:")
        for audience in audiences.keys():
            if Path(f"mkdocs.{audience}.yml").exists():
                print(f"  mkdocs serve --config-file mkdocs.{audience}.yml")
    
    print(f"\nNote: Internal navigation preserved from existing mkdocs.internal.yml")
    print("Add internal-only pages directly to mkdocs.internal.yml nav section.")
    
    if enable_advanced:
        print("Advanced audiences enabled via plugin configuration.")
    else:
        print("Simple workflow active. Enable partner/beta in plugin config if needed.")
    
    return 0 if success_count == len(audiences) else 1

if __name__ == "__main__":
    sys.exit(main())