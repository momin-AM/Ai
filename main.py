try:
    from win32com.client import Dispatch
    def speak(str1):
        speak=Dispatch(('SAPI.SpVoice'))
        speak.speak(str1)
        pass
except:
    pass

def chat(userinput):
    userinput=userinput.strip()
    print(f'\nyou : {userinput}\n')
    with open('data.txt','r') as f:
        data=f.readlines()
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
        

def teach(inp,repl):
    with open('data.txt','a') as f:
        f.write(f'\n{inp}\n{repl}')
while True:
    inp=input('==>')
    if inp=='bye':
        print('have a good day!')
        break
    elif inp=='!teach':
        inpp=input('enter password : ')
        if inpp=='momin':
            print('teaching method : you can add multiple values for userinput seperating them with ".."\n and AIoutput will have only one value so dont use ".." on AI reply')
            inp1=input('enter values to match with user input(seperate values with"..") : ')
            repl=input('enter reply for the above inputs(don"t try to seperate) : ')
            teach(inp1,repl)
    else:
        chat(inp)
