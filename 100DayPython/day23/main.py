import os
import glob

files = glob.glob('./output/*')
for f in files:
    os.remove(f)

with open("./input/format.txt") as file_format:
    format = file_format.read()

    with open("./input/invite.txt") as file_invite:
        lines = file_invite.readlines()

        for line in lines:
            line = line.replace("\n", "")
            email_content = format.replace("[name]", line)

            with open(f"./output/{line}.txt", mode="w") as file_email:
                file_email.write(email_content)



