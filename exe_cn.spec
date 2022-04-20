# -*- mode: python ; coding: utf-8 -*-

import sys
import os.path as osp
import os
block_cipher = None

# pip install pyinstaller == 5.0   
# pyinstaller exe.spec      

# 获取当前文件夹绝对位置
SETUP_DIR = os.getcwd()+"/"
doc_dir = "data/" # 非代码文件保存位置

# 批量读取文件夹内py文件
file_name = []
for root, dirs, files in os.walk(SETUP_DIR):
    for name in files:
        if name.endswith(".py"):
            if name !="no_run.py":  # 不需要执行的py文件
                file_path = os.path.join(root, name)
                file_name.append(file_path)
# 路径
pathex = [
    SETUP_DIR
]

# 手动添加库 ，例如hiddenimports = ["skimage.filter"] 
hiddenimports = [] 

# 参数设置
dir_name = "python2exe" # 保存文件夹名称
exe_name = "demo" # exe文件名
console=False  # 执行时显示终端
disable_windowed_traceback=False  

#尽量不要修改以下参数
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
