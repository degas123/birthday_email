##################### Normal Starting Project ######################
import smtplib
import random
import datetime as dt
import pandas
my_email = "jtt666664@gmail.com"
password = "Fuck_123"


today=dt.datetime.now()

today_tuple =( today.month, today.day)


data = pandas.read_csv("birthdays.csv")
persons_info = { (data_row.month, data_row.day):data_row for (index, data_row)in data.iterrows()}

if today_tuple in persons_info:
    persons_birthday = persons_info[today_tuple]
    file_path= f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path)as letter_file:
        contes=letter_file.read()
        contes= contes.replace("[NAME]",persons_birthday["name"])


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=persons_birthday["email"],
            msg= f"subject:Happybirthday\n\n {contes}"
        )


