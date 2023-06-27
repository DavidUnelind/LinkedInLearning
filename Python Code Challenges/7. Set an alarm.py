import time
import playsound

def setAlarm(alarmTime, soundFile, message):
    while time.time() < alarmTime:
        None
    playsound(soundFile)
    print(message)

setAlarm(time.time() + 5, r"Python Code Challenges\resources\alarm.mp3", "Wake up!")