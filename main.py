# imports
import os
import yagmail
import time


# p_vars: #1 resets #2 questions from start of send
with open("p_vars.txt", "r") as f:
    rawVars = f.readlines()
    resets = int(rawVars[0].strip("\n"))
    qsSinceReset = int(rawVars[1])

loopCtrl = 1

# SUB-ROUTINES
def new_question(question:str, questionsSinceReset:int):

    return questionsSinceReset + 1

def reset_questions(resets):
    with open("new_questions.txt", "w") as fQs:
        fQs.write("")
    resets += 1
    return resets

# END OF RUN - update p_vars
def write_pvars(resets, newQsSinceReset):
    with open("p_vars.txt", "w") as fPVars:
        fPVars.write(f"{resets}\n{newQsSinceReset}")


# create prompt for input - add os.system("cls") when done(ish)
print("Welcome to frOSt V0.0.5")
# write question to file - add check to see if question has response already

# Commands
while loopCtrl == 1:
    loopCtrl = 2
    prompt = input("> ")
    if prompt.lower() == "reset new questions":
        print(f"Current values are - \nResets: {resets}\nQuestions since last reset: {qsSinceReset}")
        promptConf = input("Are you sure? (yes/no): ")
        if promptConf.lower() == "yes":
            resets = reset_questions(resets)
            write_pvars(resets, 0)
            loopCtrl = 1
        else:
            loopCtrl = 1

    elif prompt == "FULL VALUE RESET":
        promptConf = input("Are you sure? (yes/no): ")
        if promptConf.lower() == "yes":
            reset_questions(resets)
            write_pvars(0, 0)
            loopCtrl = 10000
        else:
            loopCtrl = 1

    # send new_questions file to email so that file doesn't need to be stored in repo
    elif prompt == "send questions":
        print("Sending questions....")
        yag = yagmail.SMTP("milobumblehog@gmail.com", oauth2_file="~/oauth2_creds.json")
        yag.send(
            to="krill0w@duck.com",
            subject= f"Question Batch {resets}",
            contents=time.ctime(),
            attachments="new_questions.txt"
        )
        resets = reset_questions(resets)
        write_pvars(resets, 0)
        print("Questions sent")
        loopCtrl = 1

    # open files - in future this should be able to not need to be specified
    elif prompt == "open my work notes":
        filename = "Quick Notes.md"
        for root, dirs, files in os.walk("C:"):
            if filename in files:
                foundFile = os.path.join(root, filename)
                print(f"Found: {foundFile}")
                os.system(f"notepad {foundFile}")
                loopCtrl = 1


    elif prompt == "end":
        loopCtrl = 10000
    else:
        print("Prompt has not been added to the program but will be added in the future")
        with open("new_questions.txt", "a") as fQs:
            fQs.write(f"{prompt}\n")
        qsSinceReset += 1
        write_pvars(resets, qsSinceReset)
        loopCtrl = 1
