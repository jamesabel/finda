#!/usr/bin/env bash
rm -rf build dist
rm installs/*.dmg
venv/bin/python3 setup.py py2app
hdiutil create -volname finda -srcfolder dist -ov -format UDZO installs/finda.dmg
