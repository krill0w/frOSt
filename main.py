# imports
import os
import yagmail
import time


# p_vars: #1 resets #2 questions from start of send
def load_pvars():
    with open("p_vars.txt", "r") as f:
        rawVars = f.readlines()
        resets = int(rawVars[0].strip("\n"))
        qsSinceReset = int(rawVars[1])
    return resets, qsSinceReset

# SUB-ROUTINES
def reset_questions(resets):
    with open("new_questions.txt", "w") as fQs:
        fQs.write("")
    resets += 1
    return resets

def save_pvars(resets, newQsSinceReset):
    with open("p_vars.txt", "w") as fPVars:
        fPVars.write(f"{resets}\n{newQsSinceReset}")

def send_questions(resets):
    print("Sending questions....")
    yag = yagmail.SMTP("milobumblehog@gmail.com", oauth2_file="~/oauth2_creds.json")
    yag.send(
        to="krill0w@duck.com",
        subject=f"Question Batch {resets}",
        contents=time.ctime(),
        attachments="new_questions.txt"
    )
    print("Questions sent")

def open_file(filename):
    print(f"Searching for {filename}")
    for root, _, files in os.walk("C:\\"):
        if filename in files:
            found_file = os.path.join(root, filename)
            print(f"Found: {found_file}")
            os.system(f"notepad {found_file}")
            return
    print(f"{filename} not found.")


def main():
    os.system("cls")
    print("Welcome to frOSt V0.0.5")

    resets, qs_since_reset = load_pvars()
    loop_ctrl = True

    while loop_ctrl:
        prompt = input("> ").strip().lower()

        if prompt == "reset new questions":
            print(f"Current values are - \nResets: {resets}\nQuestions since last reset: {qs_since_reset}")
            if input("Are you sure? (yes/no): ").strip().lower() == "yes":
                resets = reset_questions()
                qs_since_reset = 0
                save_pvars(resets, qs_since_reset)

        elif prompt == "full value reset":
            if input("Are you sure? (yes/no): ").strip().lower() == "yes":
                resets = reset_questions()
                save_pvars(0, 0)
                loop_ctrl = False

        elif prompt == "send questions":
            send_questions(resets)
            resets = reset_questions(resets)
            qs_since_reset = 0
            save_pvars(resets, qs_since_reset)

        elif prompt == "open my work notes":
            open_file("Quick Notes.md")

        elif prompt == "end":
            loop_ctrl = False

        else:
            print("Prompt has not been added to the program but will be added in the future")
            with open("new_questions.txt", "a") as f:
                f.write(f"{prompt}\n")
            qs_since_reset += 1
            save_pvars(resets, qs_since_reset)

if __name__ == "__main__":
    main()
