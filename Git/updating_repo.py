import time
from os import system

try:
    system("git add -A")
    time.sleep(5)
    message = input("Enter commit Message: ")
    system(f"git commit -m {message}")
    time.sleep(5)
    system("git push -u origin master")
except Exception as e:
    print(e)
