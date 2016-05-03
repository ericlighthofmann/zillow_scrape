# -*- mode: python -*-

block_cipher = None


a = Analysis(['zillow_scrape.py'],
             pathex=['C:\\Users\\Eric\\desktop\\zillow_scrape-master'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='zillow_scrape',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='Hofdata.ico')
