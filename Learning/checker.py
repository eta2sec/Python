import os

import psutil

if "Todoist.exe" in (p.name() for p in psutil.process_iter()):
    print('Todoist is running!')
else:
    os.startfile("C:/Users/Evan/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Todoist")
