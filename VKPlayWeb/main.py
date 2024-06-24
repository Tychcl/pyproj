import eel
import subprocess

result = subprocess.run('netstat -ano|findstr 8000', capture_output=True, text=True, shell=True)
print(result.stdout)

eel.init('e:/prg/PyCharm Community Edition 2023.3.4/PyProj/note/pyproj/pyproj/VKPlayWeb/web')
eel.start('index.html', mode='iexplore')