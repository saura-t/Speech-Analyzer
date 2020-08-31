import speech_recognition as sr
from textblob import TextBlob
from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD
lcd=Adafruit_CharLCD(rs=26,en=19,d4=13,d5=6,d6=5,d7=11,cols=16,lines=2)
lcd.clear()
ans="yes"
while(ans=="yes"):
    with sr.Microphone() as source:
        try:
            print("Speak Anything :")
            lcd.message("\nSpeak Anything:")
            r = sr.Recognizer()
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source,timeout=20)
            lcd.clear()
            print(audio)
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            lcd.clear()
            lcd.message("{}".format(text))
            sleep(5)
            a = TextBlob(text)
            m=a.sentiment.polarity
            m+=1
            m*=50
            lcd.clear()
            print(" ",int(m))
            lcd.message("Rating: {}".format(int(m)))
            sleep(5)
        except Exception as e:
            print(e)
            lcd.clear()
            lcd.message(e)
            
    lcd.clear()
    lcd.message("Do you want to \n redo?")
    with sr.Microphone() as source:
        try:
            print("Answer:")
            lcd.message("\nAnswer:")
            r = sr.Recognizer()
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source,timeout=20)
            lcd.clear()
            print(audio)
            ans = r.recognize_google(audio)
            print("You said : {}".format(ans))
            lcd.clear()
            lcd.message("You said : {}".format(ans))
        except Exception as e:
            print(e)
            lcd.clear()
            lcd.message(e)
sleep(3)
lcd.clear()