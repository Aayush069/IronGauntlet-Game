#-----------------------------AUTHOR: Follow on Instagram @_.b_a_a_g_h_i._ -------------------------------#


import cx_Freeze
import sys
base = None
if sys.platform == "win32":
    base = "WIN32GUI"
shortcut_table = [
    ("DesktopShortcut",
    "DekstopFolder",
    "Iron Gauntlet",
    "TARGETDIR",
    "[TARGETDIR]\IRON_GAUNTLET.exe",
    None,
    None,
    None,
    None,
    None,
    "TARGETDIR",
    )
]
msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data': msi_data}

executables = [cx_Freeze.Executable(script="IRON_GAUNTLET.py", icon='icon.ico',base=base)]

cx_Freeze.setup(
    version="1.0",
    descroption="IRON MAN VS THANOS",
    author="Baaghi:-)",
    name="Iron Gauntlet",
    options={"build.exe":{"packages":["pygame"], "include files":['icon.ico','Grenade+1.mp3','Gun+Silencer.mp3','Avengers Suite (Theme) 128 kbps.mp3','icon_gauntlet.jfif','GY8Rg8f.png','ironmannew.png','thanos1.png']},
             "bdist.msi": bdist_msi_options,
             },
    executables = executables

    )


#-----------------------------AUTHOR: Follow on Instagram @_.b_a_a_g_h_i._ -------------------------------#



