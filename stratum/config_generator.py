#!/usr/bin/env python3
"""
Stratum Config Generator - Lightweight Edition
"""

import argparse
import yaml
from copy import deepcopy
from pathlib import Path
from typing import List, Dict, Any

def parse_args():
    parser = argparse.ArgumentParser(description="Generate Stratum audience-specific MkDocs configs.")
    parser.add_argument("-i", "--input", default="mkdocs.yml", help="Base mkdocs.yml path")
    return parser.parse_args()

def generate_audience_configs(base_config_path: str = "mkdocs.yml") -> List[str]:
    """Generate audience-specific configuration files."""
    print("Generating Stratum audience configurations...")
    
    path = Path(base_config_path)
    if not path.exists():
        raise FileNotFoundError(f"{base_config_path} not found")
    
    base = yaml.safe_load(path.read_text())
    
    audiences = ['public', 'internal', 'partner', 'beta']
    generated_files = []
    
    for audience in audiences:
        config = deepcopy(base)
        
        # Set audience flags
        config["extra"] = config.get("extra", {})
        config["extra"].update({
            "audience_internal": audience == "internal",
            "audience_partner": audience == "partner", 
            "audience_beta": audience == "beta",
        })
        
        filename = f"mkdocs.{audience}.yml" if audience != 'public' else "mkdocs.public.yml"
        
        with open(filename, "w") as f:
            yaml.dump(config, f, sort_keys=False, default_flow_style=False)
        
        generated_files.append(filename)
        print(f"Generated {filename}")
    
    return generated_files

def main():
    try:
        args = parse_args()
        files = generate_audience_configs(args.input)
        print(f"\nSuccess! Generated {len(files)} configurations.")
        print("\nTest commands:")
        print("   mkdocs serve --config-file mkdocs.public.yml")
        print("   mkdocs serve --config-file mkdocs.internal.yml") 
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == '__main__':
    import sys
    sys.exit(main())