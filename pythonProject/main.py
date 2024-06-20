import eel

#netstat -ano|findstr 4444
#tskill [ласт цифра команды выше]

eel.init("web")
eel.start("main.html", size=(300, 600))
