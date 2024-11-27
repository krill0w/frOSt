import os
import yagmail

#create prompt for input
os.system("cls")
print("Welcome to frOSt V0.0.1")
prompt = input("> ")

# write question to file - add check to see if question has response already
f = open("new_questions.txt", "a")
f.write(prompt)
f.close()

# send new_questions file to email so that file doesn't need to be stored in repo
yag = yagmail.SMTP("milobumblehog@gmail.com", oauth2_file="~/oauth2_creds.json")
yag.send(
    to="dom@kalowe.me.uk",
    subject="Yagmail test for questions",
    contents="Please find attached the questions", 
    attachments="new_questions.txt",
)


# handle actions for prompts
if prompt.isdigit():
    prompt = int(prompt)

