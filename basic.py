import os.path
from json import load
import json

def Read_file(file):
    f=open(file, "r")
    Data=f.read()
    f.close()
    return Data

def Write_file(file, Data):
    f=open(file, "w")
    f.write(Data)
    f.close()

def Append_file(file, Data):
    f=open(file, "a")
    f.write(Data)
    f.close()

def Create_file(file):
    Data = ""
    f=open(file, "w")
    f.write(Data)
    f.close()

def Checkpath(path):
    if os.path.exists(path):
        return True
    else:
        return False

def getConfig(file, name):
    with open(file, "r") as f:
        json_file = json.load(f)
        return json_file[name]
