import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import sys
import pyautogui
import time
import smtplib
# from win32com.client import Dispatch

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#-----------FUCNTIONS------------#
def speak(msg):
    engine.say(msg)
    engine.runAndWait()

def chat(userinput):
    userinput=userinput.strip()
    print(f'\nyou : {userinput}\n')
    success=False
    for lists in data:
        listss=lists.strip().split('..')
        if userinput in listss:
            temp1=data.index(lists)
            print(f'jango : {data[temp1+1].strip()}\n')
            try:
                speak(data[temp1+1].strip())
            except:
                pass
            success=True
            break
    if success is False:
        print('sorry i dont understand, if you wanna teach me about this type "!teach"')
        try:
            speak('sorry i dont understand, if you wanna teach me about this type "!teach"')
        except:
            pass
        
def teach():
    file_path = 'data.txt'
    new_input = input('Enter questions: ')
    reply = input('Reply: ')
    new_input_list = new_input.strip().split('..')
    found = False
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            line_content = line.strip().split('..')
            line_updated = False  # Flag to check if the line was updated
            
            for item in new_input_list:
                if item in line_content:
                    # Remove the existing element from the input list
                    new_input_list.remove(item)
                    line_content.extend(new_input_list)
                    line = '..'.join(line_content) + '\n'
                    line_updated = True
                    break

            if line_updated:
                file.write(line)
                found = True
            else:
                file.write(line)
        
        # Append the new input and reply as a new line if no matching element was found
        if not found:
            file.write(f'{new_input}\n{reply}\n')

def wishme():
    hour=int(datetime.datetime.now().hour)
    if 4<hour<=11:
        speak('good morning')
        print('good morning')
    elif 11<hour<=15:
        speak('good noon')
        print('good noon')
    elif 15<hour<=18:
        speak('good afternoong')
        print('good afternoon')
    elif 18<hour<20:
        speak('good evening')
        print('good evening')
    else:
        print('good night')
        speak('good night')

def takecommand():
    '''it takes microphone input and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('recognising...')
        query=r.recognize_google(audio,language='en-in')
        print(f'user : {query}\n')
    except Exception as e:
        print('say that again please...')
        return 'None'
    return query

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('myemail@gmail.com','password')
    server.sendmail('myemail@gmail.com',to,content)
    server.close()

with open('data.txt','r') as f:
        data=f.readlines()
pwd=(os.getcwd())

#-------------CODE STARTS------------#
if __name__=='__main__':
    wishme()
    # speak('type 1 for texting and 2 for talking')
    inp0=input('enter : ')
    while True:
        if inp0=='1':
            user_input=input('==>')
            query=user_input
        elif inp0==2:
            query=takecommand().lower
        elif inp0=='0':
            break
        else: 
            print("type only '1' or '2'")
            speak('type only 1 or 2')
        if 'wikipedia' in query:
            speak('searching on wikipedia')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=1)
            speak('according to wikipedia')
            print(results)
            speak(results)
        elif query in ['stop','bye','turn off','stop jarvis']:
            speak('good bye')
            break
        elif query in ['restart','restart yourself']:
            speak('restarting...')
            os.system(f'python {pwd}/jarvis/main.py')
            sys.exit()
        elif (query[:5])=='start':
            speak(f'opening {query[6:]}')
            try:
                os.system(f'start {query[6:]}')
            except: 
                print('something went wrong') 
                speak('something went wrong')
        elif (query[:4])=='open':
            speak(f'opening {query[5:]}')
            try:
                os.system(f'start {query[6:]}')
            except: 
                print('something went wrong') 
                speak('something went wrong')
        elif 'play music' in query:
            os.system(f'start msedge spotify.com')
            time.sleep(7)
            pyautogui.click(933, 944)
            time.sleep(2)
            pyautogui.click(1781, 25)
        elif any(i in query for i in ['time', 'the time', 'current time']):
            print(f'time now -> {(datetime.datetime.now().hour)}:{(datetime.datetime.now().minute)}')
            speak(f'its {(datetime.datetime.now().hour)}:{(datetime.datetime.now().minute)}')
        elif 'send email' in query or 'email' in query:
            try:
                speak('what should i write')
                inp_temp=input('1.type 2.voice : ')
                if inp_temp=='1':
                    writing=input('text : ')
                elif inp_temp=='2':
                    writing=takecommand()
                else:
                    speak('wrong choice')
                to=f'{query[6:]}@gmail.com'
                sendemail(to,writing)
                speak('email sent')
            except Exception as e:
                print(e)
                speak('something went wrong')
        elif query=='!teach':
            teach()
        else:
            chat(query)
                
                


        


