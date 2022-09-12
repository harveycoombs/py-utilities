#2015-2022 Harvey Coombs | A selection of useful tools.
import os
import random
import sys

def rename_file(cur_dir, subject):
    snake_name = (subject.replace(" ", "_")).lower()
    os.rename(f"{cur_dir}\\{subject}", f"{cur_dir}\\{snake_name}")

def snakeify():
    print("1. Target directory [DEFAULT: current dir]:")
    dir_choice = input() #CHANGED: raw_input() to input()

    if len(dir_choice) == 0:
        dir_choice = os.getcwd()

    the_dir = os.listdir(dir_choice)
    omitted = 0

    for the_file in the_dir:
        if not the_file == "snakeify.py":
            rename_file(dir_choice, the_file)
        else:
            omitted += 1

    print(f"{(len(the_dir) - omitted)} File(s) snakeified. ({omitted} Omitted)")

def generate_pw(length):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!!£$%^&*()_+-=[];'#,./\{\}:@~<>?"
    pw = ""

    for j in range(int(length)):
        x = int(random.random() * len(chars))
        pw += tuple(chars)[x]

    print(pw)

if sys.argv[1] == "-pw":
    generate_pw(sys.argv[2])
elif sys.argv[1] == "-sk":
    snakeify(sys.argv[2])
else:
    print("Invalid command")
