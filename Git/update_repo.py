import time
from os import system

def update():
    try:
        # message = input("Enter commit Message: ")
        message = "Updated"
        print("Adding all files...")
        system("git add -A")
        print("Files added")
        print("Committing...")
        system(f'git commit -m "{message}"')
        print("Committed")
        print("Pushing repo")
        system("git push -u origin master")
        print("Repo successfully Updated")
    except Exception as e:
        print(e)


while True:
    update()
    do:print(".")
    while (time.sleep(120));
