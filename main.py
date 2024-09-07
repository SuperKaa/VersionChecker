import requests
from colorama import Fore, init
import time
import datetime

init()

def thetime():
    global timenow
    current_time = datetime.datetime.now()
    current_hour = current_time.hour
    current_minute = current_time.minute
    current_second = current_time.second
    timenow = f"[{current_hour}:{current_minute}:{current_second}]"
    return timenow


thetime()
print(Fore.YELLOW + f"{timenow} Attempting To Get Version Info, Will Close If Network Is Unavailable.")

time.sleep(1)

def pastebin_content(link):
    response = requests.get(link)
    if response.status_code == 200:
        return response.text
    else:
        thetime()
        print(Fore.RED +  f"{timenow} Network Error")
        return None

pastebin_link = "YOUR PASTEBIN LINK"                # PUT YOUR PASTEBIN LINK HERE (when making the pastebin just put the words "inactive" or "active")
status = pastebin_content(pastebin_link)

if status == "inactive":
    thetime()
    print(Fore.RED +  f"{timenow} Your Version Is Outdated")
    time.sleep(0.2)
    thetime()
    print(Fore.RED +  f"{timenow} Exitting in 5...")
    time.sleep(5)
    exit()

elif status == "active":
    thetime()
    print(Fore.GREEN + f"{timenow} Version Active")
    time.sleep(0.2)

else:
    thetime()
    print(Fore.RED +  f"{timenow} Network Error")
    time.sleep(1)
    thetime()
    print(Fore.RED +  f"{timenow} Exitting in 5...")
    time.sleep(5)
    exit()


# your code goes here 


print("your code here")
time.sleep(10)
