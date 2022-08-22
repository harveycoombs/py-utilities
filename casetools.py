#2015-2022 Harvey Coombs | rename your files to conform to 'snake_case'!
import os

def rename_file(cur_dir, subject):
    snake_name = (subject.replace(" ", "_")).lower()
    os.rename(f"{cur_dir}\\{subject}", f"{cur_dir}\\{snake_name}")

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