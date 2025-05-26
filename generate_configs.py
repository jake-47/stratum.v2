#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    from stratum.config_generator import main as stratum_main
    sys.exit(stratum_main())
except ImportError as e:
    print(f"Import error: {e}")
    print("   Run: pip install -e .")
    sys.exit(1)