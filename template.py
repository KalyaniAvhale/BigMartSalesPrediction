'''
#This script creates the Project Structure Files

author : Kalyani Avhale
version : 0.0.1

'''
import os

dirs = [
    os.path.join("data","data_given"),
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src",
    "prediction_service",
    "test",
    "webapp",
    os.path.join("webapp","static"),
    os.path.join("webapp","templates")
]

for dir_ in dirs:
    os.makedirs(dir_ , exist_ok=True)
    with open(os.path.join(dir_ , ".gitkeep"),"w") as f:
        pass

files= [
    "README.md",
    "dvc.yaml",
    "params.yaml",
    os.path.join("src","__init__.py"),
    "app.py"
]

for file_ in files:
    with open(file_ , "w") as f:
        pass