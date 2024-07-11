fitz_init_path = "/app/.heroku/python/lib/python3.12/site-packages/fitz/__init__.py"

with open(fitz_init_path, "r") as file:
    lines = file.readlines()

with open(fitz_init_path, "w") as file:
    for line in lines:
        if "from frontend import *" not in line:
            file.write(line)
