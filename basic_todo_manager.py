#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 16:59:30 2025

@author: shivam
"""
import argparse
import json

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def update_task(index, new_task):
    if 0 <= index < len(tasks):
        tasks[index] = new_task
        print(f"Task updated: {new_task}")
    else:
        print("Invalid task index")

def delete_task(index):
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Task deleted: {deleted_task}")
    else:
        print("Invalid task index")

def list_tasks():
    for idx, task in enumerate(tasks):
        print(f"{idx}: {task}")

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index] = f"[Completed] {tasks[index]}"
        print(f"Task marked as completed: {tasks[index]}")
    else:
        print("Invalid task index")

def calculator(operation, num1, num2):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Invalid operation."
    return f"Result of {operation}: {result}"

def main():
    load_tasks()

    parser = argparse.ArgumentParser(description="Simple To-Do List Manager and Calculator")
    parser.add_argument("command", help="Command to execute (add, update, delete, list, complete, calc)")
    parser.add_argument("task_or_index", help="The task description or task index, or operation", nargs="?")
    parser.add_argument("new_task_or_num1", help="The new task description or first number", nargs="?")
    parser.add_argument("num2", help="The second number (for calculator only)", type=float, nargs="?")
    args = parser.parse_args()

    if args.command == "list":
        list_tasks()
    elif args.command == "add":
        if args.task_or_index:
            add_task(args.task_or_index)
            save_tasks()
        else:
            print("Please provide a task to add.")
    elif args.command == "update":
        if args.task_or_index and args.new_task_or_num1:
            update_task(int(args.task_or_index), args.new_task_or_num1)
            save_tasks()
        else:
            print("Please provide a task index and new task description to update.")
    elif args.command == "delete":
        if args.task_or_index:
            delete_task(int(args.task_or_index))
            save_tasks()
        else:
            print("Please provide a task index to delete.")
    elif args.command == "complete":
        if args.task_or_index:
            complete_task(int(args.task_or_index))
            save_tasks()
        else:
            print("Please provide a task index to mark as complete.")
    elif args.command == "calc":
        if args.task_or_index and args.new_task_or_num1 and args.num2 is not None:
            operation = args.task_or_index
            num1 = float(args.new_task_or_num1)
            num2 = args.num2
            print(calculator(operation, num1, num2))
        else:
            print("Please provide an operation (add, subtract, multiply, divide) and two numbers.")
    else:
        print("Invalid command. Use 'add', 'update', 'delete', 'list', 'complete', or 'calc'.")

if __name__ == "__main__":
    main()
