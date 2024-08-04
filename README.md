# AO-opgave
et repro for test opgaven fra AO 

Før du prøver systemet er det nødvendigt at du har modules fra requirements.txt installeret 
pip install -r .\AO-opgave-main\requirements.txt

for at prøve teste koden skal ud sikre dig at du er i samme directory som main.py filen og udføre følgende komando 
uvicorn main:app --reload
hvis du får beskeden Error loading ASGI app. could not import module "main" så er du ikke i det korete directory

Når systemet kører kan du gå til http://127.0.0.1:8000/ og begynde at teste. 

Link til demo video: https://youtu.be/F-9-0nzfucU