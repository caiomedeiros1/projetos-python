from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "testesmtp836@gmail.com"
MY_PASSWORD = "qxdl avjw unyc nsiz"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row  for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    file_path = f"letter{random.randint(1,2)}.txt"
    birthday_person = birthdays_dict[today_tuple]
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=birthday_person["email"],
            msg="Subject:Happy Birthday!\n\n")