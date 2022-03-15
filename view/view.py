# Import needed library
from colorama import Fore
from os import system, name
from time import sleep



# Main logo
def main_banner():
    system('cls' if name == 'nt' else 'clear') # Clear Screen
    print(Fore.RED + """
                          
    ____                                                 __            
   / __ \____ ___________   ____ ____  ____  _________ _/ /_____  _____
  / /_/ / __ `/ ___/ ___/  / __ `/ _ \/ __ \/ ___/ __ `/ __/ __ \/ ___/
 / ____/ /_/ (__  |__  )  / /_/ /  __/ / / / /  / /_/ / /_/ /_/ / /    
/_/    \__,_/____/____/   \__, /\___/_/ /_/_/   \__,_/\__/\____/_/     
                         /____/                                        


          """)

    
# Print menu
def menu():
    sleep(0.05)
    print(Fore.RED + ' [' + Fore.WHITE + '#' + Fore.RED + ']' + Fore.BLUE + " Choose one of the options below\n")
    sleep(0.05)
    print(Fore.YELLOW + ' [1] Generate new password')
    sleep(0.05)
    print(Fore.MAGENTA + ' [2] Password list')
    sleep(0.05)
    print(Fore.GREEN + ' [3] Export password data')
    sleep(0.05)
    print(Fore.CYAN + ' [4] Remove password')
    sleep(0.05)
    print(Fore.RED + ' [0] Exit...' + Fore.RESET)
    

# Select user   
def select(text, title):
    sleep(0.03) # 0.03s sleep
    try:
        # Print input text and turn it into number and return base
        return input(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "Pass Generator "+ Fore.GREEN + "~ " + Fore.BLUE + title + Fore.GREEN +" <<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] "+ Fore.YELLOW + text + Fore.RESET + " ")
    except:
        # In the event of incoming number
        return -1
    
    
def show(text, text2):
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "Pass Generator "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.YELLOW + text + Fore.GREEN + text2) 
    
    
# Get the status of the user to continue the program n => exit || other get => continue
def status():
    return input(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "Pass Generator "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.YELLOW + 'Do you want to continue?('+ Fore.RED + 'n' + Fore.YELLOW + '/no || other/yes) ' + Fore.RESET)
    
    
# Show history extract
def history(data):
    main_banner() # Show main banner and clear screen
    
    count = 0 # For color show
    for i in data:
        i = i.split(',')
        if count % 2 == 0: # Yellow text
            print(Fore.GREEN + ' [' + Fore.WHITE + str(count + 1) + Fore.GREEN + '] ' + Fore.WHITE + i[0] + Fore.RESET + ' => ' + Fore.YELLOW + i[1])
        else: # Red text
            print(Fore.GREEN + ' [' + Fore.WHITE + str(count + 1) + Fore.GREEN + '] ' + Fore.WHITE + i[0] + Fore.RESET + ' => ' + Fore.RED + i[1])
        count += 1


# Print Good Bye :)
def bye():
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "Pass Generator "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "!" + Fore.RED +"] " + Fore.YELLOW + 'We hope you enjoy the Password Generator')


# Wrong Input
def wrong():
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "Pass Generator "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.YELLOW + 'The input structure has not been observed !!')


# Main Menu
def main():
    main_banner()
    menu()
    