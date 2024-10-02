import os 
from pathlib import Path

while True:
    project_name = input("Enter the Src Folder Name:")
    if project_name != '':
        break

list_of_files = [
    ".github/workflows/.gitkeep",
     f"{project_name}/__init__.py",
     f"{project_name}/components/data_ingestion.py",
     f"{project_name}/components/data_preprocessing.py",
     f"{project_name}/components/model_loading.py",
     f"{project_name}/pipeline/inference.py",
     f"{project_name}/pipeline/training.py",
     f"{project_name}/exception.py",
     f"{project_name}/logger.py",
     "templates/index.html",
     "statics/style.css",
     "notebook/research.ipynb",
     "init_setup.sh",
     "requirements.txt",
     "Dockerfile",
     "setup.py"
     "app.py",
     

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
