# -*- mode: python ; coding: utf-8 -*-
import sys

block_cipher = None

# Add static linking options for Linux
if sys.platform.startswith('linux'):
    from PyInstaller.building.api import EXE, PYZ
    import os
    
    # Set environment variables for static linking
    os.environ['LDFLAGS'] = '-static -static-libgcc -static-libstdc++'
    os.environ['CFLAGS'] = '-static'

a = Analysis(
    ['src/portfinder/portfinder.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['psutil', 'rich', 'rich.table', 'rich.console', 'rich.text'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='portfinder',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,  # Strip symbols
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # Try to link statically on Linux
    **({'link_args': ['-static']} if sys.platform.startswith('linux') else {})
)