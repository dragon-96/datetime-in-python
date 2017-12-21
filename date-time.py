"""
this   is to create datime format file
"""
import datetime

filename=datetime.datetime.now()
def create_file():
    """this creates an empty file"""
    with open(filename.strftime("%d-%B-%Y-%H-%M")+".txt","w") as file:
        file.write(" ")

create_file()
