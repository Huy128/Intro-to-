import pyttsx3
from Task1 import task1
from Task1 import a
class task3(task1):
    def __init__(self):
        super().__init__()
        self.engine = 0
    def voice_actor(self):
        self.c = a
        if (self.c == 1):
            self.engine = pyttsx3.init()
            self.engine.say("please wear a face mask")
            self.engine.runAndWait()
        elif (self.c == 2):
            self.engine = pyttsx3.init()
            self.engine.say("you are pass, please come in")
            self.engine.runAndWait()

Task3 = task3()

Task3.voice_actor()
