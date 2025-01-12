# CLI To-Do Manager

A simple command-line interface (CLI) to-do list manager and calculator built with Python.

## Features
- Add, update, and delete tasks
- List all tasks
- Mark tasks as complete
- Basic calculator for arithmetic operations

## Requirements
>Python IDE
>Argparse library in python

## Prerequisites
>A bit of python knowledge
>A happy mind

## Installation
1. Download the python script with name **basic_todo_manager.py** .
2. Activate Your Virtual Environment

   *Open your terminal or command prompt.*

   *Navigate to your virtual environment directory*
   ```sh
       cd path/to/your/directory

3. **Run the Python script with the desired command.**
   **Some examples are**
     ## Add Tasks
   - **Command**: 
  > add
  - **Description**: Adds a new task to the to-do list.
  - **Example**:
    ```sh
    python basic_todo_manager.py add "Buy groceries"
    ```
  - **Output**:
    ```
    Task added: Buy groceries
    ```
    ## Update Tasks
      - **Command**: 
    > update
    - **Description**: Updates an existing task at the specified index.
  - **Example**:
    ```sh
    python basic_todo_manager.py update 0 "Buy milk"
     ```
  - **Output**:
    ```
    Task updated: Buy milk
    ```
  ## Calculator
  - **Command**
    > calc
  - **Description**: Performs basic arithmetic operations (add, subtract, multiply, divide) between two numbers.
  - **Example**:
    ```sh
    python basic_todo_manager.py calc add 10 5
    ```
 - **Output**
   ```
   Result of add: 15.0
   ```
