# -*- mode: python ; coding: utf-8 -*-

import sys
import os.path as osp
import os
block_cipher = None

# pip install pyinstaller == 5.0   
# pyinstaller exe.spec      

# Get the absolute location of the current folder
SETUP_DIR = os.getcwd()+"/"
doc_dir = "data/" # Where to save non-code files

# Batch read py files in a folder
file_name = []
for root, dirs, files in os.walk(SETUP_DIR):
    for name in files:
        if name.endswith(".py"):
            if name !="no_run.py":  # py file that does not need to be executed
                file_path = os.path.join(root, name)
                file_name.append(file_path)
# path
pathex = [
    SETUP_DIR
]

# Add the library manually, just like hiddenimports = ['skimage.filters'] 
hiddenimports = [] 

# parameter settings
dir_name = "python2exe" # save folder name
exe_name = "demo" # exe file name
console=False  # Display terminal while executing
disable_windowed_traceback=False  


# Try not to modify the following parameters
a = Analysis(
    file_name,
    pathex=pathex,
    binaries=[],
    datas=[(SETUP_DIR+doc_dir,doc_dir)],
    hiddenimports=[],
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
    [],
    exclude_binaries=True,
    name=exe_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=console,
    disable_windowed_traceback=disable_windowed_traceback,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=dir_name,
)
