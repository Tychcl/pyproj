import eel
import subprocess
import winreg
import re

def get_default_browser_windows():
    browser_path = ""
    try:
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"HTTP\shell\open\command")
        browser_path, _ = winreg.QueryValueEx(key, "")
        winreg.CloseKey(key)
        browser_name = re.findall(r'\"(.*?)\"', browser_path)[0].split("\\")[-1]
        browser_name = browser_name.replace(".exe", "")
    except WindowsError:
        browser_name = "Неизвестно"
    return browser_name

#netstat -ano|findstr 8000
#tskill [pid]

# Команда для выполнения
command = 'netstat -ano|findstr 8000'

# Выполнение команды и получение результата
result = subprocess.run(command, capture_output=True, text=True, shell=True)
print(result.stdout)

print(get_default_browser_windows())

eel.init('web')
eel.start('main.html', size=(300, 600), mode=get_default_browser_windows())