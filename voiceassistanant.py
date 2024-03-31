import pyttsx3 # Convert Text To Speech
import speech_recognition as sr
import webbrowser #For Searching Web
import datetime 

def speech2text():
    recognizer = sr.Recognizer() #calling Recognizer Class
    with sr.Microphone() as source:
        print("Listening...") 
        recognizer.adjust_for_ambient_noise(source) # Noice removing from source
        audio = recognizer.listen(source)
        #Reading Data
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print (f'You Said: {data}')
            return data
        except sr.UnknownValueError:
            print("Not Undestand")
            
            
def text2speech(x):
    t2s = pyttsx3.init() #calling init function
    voices = t2s.getProperty('voices') 
    t2s.setProperty('voice', voices[0].id) #choosing voice with index
    rate = t2s.getProperty('rate') # / setting speed
    t2s.setProperty('rate', 150)
    t2s.setProperty('volume', 0.5)#  / setting volume
    t2s.say(x)
    t2s.runAndWait()
    
    #split program / fun
if __name__ == '__main__':
    
    if speech2text().lower() == "hello" or speech2text().lower() == "hello hello":
        data1 = speech2text().lower()
        
        if "time" in data1:
           time = datetime.datetime.now().strftime("%X")    
           text2speech(f"Sir, the time is {time}")
           print(time)
        elif "date" in data1:
            date = datetime.datetime.now().strftime("%x") 
            text2speech(date)
            print(date)
        elif 'youtube' in data1 or 'google' in data1 or 'instagram' in data1 or 'facebook' in data1 or 'twitter' in data1:
            if data1 == 'youtube':
                webbrowser.open("https://www.youtube.com")
            elif data1 == 'google':
                webbrowser.open("https://www.google.com")
            elif data1 == 'instagram':
                webbrowser.open("https://www.instagram.com")
            elif data1 == 'facebook':
                webbrowser.open("https://www.facebook.com")
            elif data1 == 'twiteer':
                webbrowser.open("https://www.twitter.com")
            
        
    else:
        print("Thank You")