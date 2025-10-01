import os
import shutil
import re 
import requests 
from datetime import datetime 

# fixed url 
url = "https://www.python.org/"
folder = "webpage_titles"
if not os.path.exists(folder):
    os.makedirs(folder)
log_file = os.path.join(folder, "titles.txt")
backup_folder = os.path.join(folder, "backup")
if os.path.exists(log_file):
    if  not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copy(log_file, os.path.join(backup_folder, f"titles_{timestamp}.txt"))
response = requests.get(url)
html = response.text
match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)
title = match.group(1) if match else "No title found"
with open(log_file, "w", encoding="utf-8") as f:
    f.write(f"URL: {url}\n")
    f.write(f"Title: {title}\n")
    f.write(f"Saved on: {datetime.now()}\n")
print("Title saved successfully!")


