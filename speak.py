import pyttsx3
robo = pyttsx3.init()
robo.say("hello sir, how are you")
robo.runAndWait()
response = input(" ")
if response == "i am fine":
    robo.say("great")
else:
    robo.say("bad")
robo.runAndWait()