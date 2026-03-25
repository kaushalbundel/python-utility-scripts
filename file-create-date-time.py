#!/usr/bin/env python3

'''
A small script for creating a simple text file so that daily task logging can be done in a simple manner.

Spec:
- Asks for a file extension
- creates a file in an existing folder
- Nomenclature of the file is yyyy-mm-dd.[extension]
'''
import datetime

def create_dated_file():
    extension: str = input("Enter the desired file-extension(default is .md): ").strip() or ".md"

    # remove the leading dot in case extension is typed with a dot
    if extension.startswith("."):
        extension = extension[1:]

    # getting current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    #creating file name
    file_name = f"{current_date}.{extension}"
    
    #file creation
    try:
        with open(file_name, 'x') as f:
            print(f"Success! File {file_name} has been created.")
    except FileExistsError:
        print(f"Error: The {file_name} already exists.")


if __name__ == "__main__":
    create_dated_file()
