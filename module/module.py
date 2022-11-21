import view.view as view
from time import sleep
from random import sample
from cryptography.fernet import Fernet


DATA = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890><?/:"L{|})(_+-=#@$&![%]*'
# you can convert code to marshal code to hide password
KEY = b'bX1Wt_qoUmUN-hxEM8CriI5O9XqvGGC_SIar1So9AHg='
fernet = Fernet(KEY)


def write(name,password):
    data = get_data()
    data.append("{},{}".format(name, password))
    
    data = bytes("\n".join(data), 'utf-8')
    data = fernet.encrypt(data)
    
    with open("data/password.txt", "w+") as file:
        file.write(str(data))


def get_data():
    try:
        with open('data/password.txt') as f:
            data = f.read()
        data = data.replace("b'", "")
        data = data.replace("'", "")
            
        data = fernet.decrypt(bytes(data, encoding='utf8')).decode("utf8").split("\n")
            
        data = [d.strip() for d in data]
        
        return data
    except:
        return []


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
    
    view.show('The Operation was successful','')
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

    view.show('Data was successfully export','')
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