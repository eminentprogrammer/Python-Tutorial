import time
from os import system

try:
    system("git add -A")
    time.sleep(2)
    message = input("Enter commit Message: ")
    system(f'git commit -m "{message}"')
    time.sleep(2)
    system("git push -u origin master")
    time.sleep(5)
    print("successfully pushed")
except Exception as e:
    print(e)