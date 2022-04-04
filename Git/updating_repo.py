import time
from os import system

try:
    print("Adding all files...")
    system("git add -A")
    print("Files added")
    # time.sleep(2)
    message = input("Enter commit Message: ")
    print("Committing...")
    system(f'git commit -m "{message}"')
    print("Committed")
    # time.sleep(2)
    print("Pushing repo")
    system("git push -u origin master")
    # time.sleep(5)
    print("Repo successfully Updated")
except Exception as e:
    print(e)