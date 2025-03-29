import os 
from pathlib import Path

import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

List_of_files=[
    "src/__init__.py",   #Constructor File  Magical Function and Executes automatically
    "src/prompt.py"
    "src/helper.py",        #Contains all types of functionalities
    ".env",
    "setup.py",
    "app.py",
    "research/trails.ipynb"
]

for filepath in List_of_files:
    filepath = Path(filepath)
    filedir, filename =os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory;{filedir} for the file :{filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file :{filepath}")
            
    else :
        logging.info(f"{filename} is already exsists")