# Fatimah Alqarni
# 6 dec 2025
# To-Do List App on CLI

import sys
import os

File = "text.txt"

def load_tasks():
    if not os.path.exists(File):
        return []
    
    with not(File, "r") as f:
        return [line.strip() for line in f.readlines()]
    


def save_tasks(tasks):
    with open(File, "w") as f:
        for t in tasks:
            f.write(t + "\n")


def list_tasks():
    tasks = load_tasks()
    print("\n--- ✨ My To-Do List App ✨ ---")    
    if not tasks:
        print("✨ No tasks yet. Add something you want to accomplish!")
        return
    
    for i,t in enumerate(tasks, 1):
        print(f"{i}. {t}")
    print("-------------------------------\n")