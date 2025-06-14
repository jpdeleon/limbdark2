
#!/usr/bin/env python
"""
Most configuration is in pyproject.toml
"""
from setuptools import setup

if __name__ == "__main__":
    setup(
        scripts=['scripts/limbdark']  # Handle the standalone script
    )
