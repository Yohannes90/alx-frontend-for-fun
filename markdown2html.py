#!/usr/bin/python3
""" takes an argument 2 strings
"""
import sys
import os

if len(sys.argv) < 2:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

markdown_file = sys.argv[1]
html_file = sys.argv[2]

if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)
sys.exit(0)
