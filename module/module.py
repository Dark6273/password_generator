import view.view as view
from time import sleep
from random import sample


DATA = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890><?/:"L{|})(_+-=#@$&![%\]*'


def write(name,password):
    file = open('data/password.txt', 'a+')
    
    text=name + ',' + password + '\n' 
    file.write(text)
    file.close()


def get_data():
    with open('data/password.txt') as f:
        data = f.readlines()
        
    data = [d.strip() for d in data]
    
    return data


def remove(data):
    ls = []
    
    name = view.select('Enter your password name (* => All) ', 'Remove')
    
    if name == '*':
        open('data/password.txt', 'w').close()
    else:
        for d in data:
            n = d.split(',')[0]
        
            if n == name:
                pass
            else:
                ls.append(d)
        
        file = open('data/password.txt', 'w')
        
        for i in ls:
            file.write(i + '\n')
        file.close()
    
    view.show('The Operation was successfull','')
    sleep(1)
    main()


def export(data):
    file = open('Password.txt', 'w+')
    file.write('Name: Password\n---------------\n\n')
    
    for d in data:
        d = d.split(',')
        text = d[0] + ": " + d[1] + '\n'
        file.write(text)
    
    file.close()

    view.show('Data was succlessfully export','')
    sleep(1)
    status()


def history(data):
    view.history(data)
    sleep(1)
    status()    


def status():
    stt = view.status()
    
    if stt == 'n':
        bye()
    else:
        main()


def generate():
    name = view.select('Password name ', 'Name')
    
    try:
        count = int(view.select('Password length ', 'Length'))
    except:
        wrong()
        
    try:
        password = ''.join(sample(DATA, count))
    except:
        wrong()
        
    write(name, password)
    
    view.show('Password created successfully  ' , name + " => " + password)
    sleep(2)
    
    status()


def bye(): # Exit from app
    view.bye()
    sleep(1)
    exit()


def wrong(): # Wrong select
    view.wrong()
    sleep(1)
    main()


def main():
    view.main()
    
    try:
        select = int(view.select("Select the option you want  ", 'Select'))
    except:
        wrong()
        
        
    if select == 1:
        generate()
    elif select == 2:
        history(get_data())
    elif select == 3:
        export(get_data())
    elif select == 4:
        remove(get_data())
    elif select == 0:
        bye()
    else:
        wrong()