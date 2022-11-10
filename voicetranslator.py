from playsound import playsound as PS  
import speech_recognition as s_r   
from googletrans import Translator as Trans   
from gtts import gTTS   
import os  
import pyaudio
dic_language=('english','en','german','de','french','fr','persian','fa','japanese','ja')
# First, we will capture the user's Voice command  
# It will take the command through built-in microphone of the device  
def take_command():  
    r1 = s_r.Recognizer()  
    with s_r.Microphone() as source:  
        print ("listening to the voice...")  
        r1.pause_threshold = 1  
        audio1 = r1.listen(source)  
    
    try:  
        print ("Recognizing the voice...")  
        query_1 = r1.recognize_google(audio, language = 'en-fr')  
        print (f" user said? {query_1}\n")  
    except Exception as ep:  
# just in case it didn't recognise the voice or language properly  
        print ("The user is requested to please say that again...")  
        return "None"  
    return query_1  
# Here, we will take the user's voice input from the user end  
query_1 = take_command()  
while (query_1 == "None"):  
    query_1 = take_command()  
  
def destination_language():  
    print("Please enter the language in which you want to convert the above input  Ex. English, German, French etc.")  
    print()  
    
    # Now, we will implement the input destination language in which the user  
# wants to translate the voice command:  
    to_language = take_command()  
    while (to_language == "None"):  
        to_language = take_command()  
    to_language = to_language.lower()  
    return to_language  
    
to_language = destination_language()  
    
# Now, we will map the input destination language with the code  
while (to_language not in dic_language):  
    print ("The language in which the user wants to convertthe voice command\ is currently not available, the user is requested to input some other language")  
    print()  
    to_language = destination_language()  
    
to_language = dic_language[dic_language.index(to_language)+1]  
# Here, we will invoke the Google Translator  
translator1 = Trans()  
# Now we will translate from src to dest  
text_to_translate_1 = translator1.translate1(query_1, dest = to_language)  
text1 = text_to_translate_1.text  
# We will be using the Google-Text-to-Speech i.e., gTTS() function of the gtts  
# module for speaking the translated text into the input destination language  
# selected by the user which is stored in to_language.  
# We have also given third argument as False because it speaks very slowly by # default  
speak = gTTS(text = text1, language = to_language, slow = False)  
    
# We will be using the save() function for saving the translated speech in #captured_JTP_voice.mp3 file  
speak.save("captured_JTP_voice.mp3")  
    
# Now at last, we will be using the OS module for running the translated voice.  
PS('captured_JTP_voice.mp3')  
os.remove('captured_JTP_voice.mp3')  
print(text)
