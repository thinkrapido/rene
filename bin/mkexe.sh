#!/usr/bin/env bash
python -m nuitka --linux-onefile-icon=`pwd`/bin/python.xpm --onefile rene/main.py
mkdir dist 2>/dev/null
mv main.bin dist/rene
