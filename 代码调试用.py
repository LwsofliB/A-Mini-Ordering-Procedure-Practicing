import time as t
import json as j


def get_int(prompt):
    while True:
        s = input(prompt).strip()
        if s == "":
            print("You haven't input anything in here!")
            continue
        try:
            return int(s)
        except ValueError:
            print("Please enter a valid integer!")



            
