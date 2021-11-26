import pandas
import random
from datetime import datetime
import smtplib

USERNAME = 'dummyman567@gmail.com'
PASSWORD = 'iamdummy13'

today = (datetime.now().month, datetime.now().day)
data = pandas.read_csv('birthdays.csv')
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    with open(file_path) as letter:
        contents = letter.read()
        modified_content = contents.replace('[NAME]', birthday_person['name'])
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(USERNAME, PASSWORD)
        connection.sendmail(from_addr=USERNAME,
                            to_addrs=birthday_person['email'],
                            msg=f"Subject:Happy Birthday {birthday_person['name']}\n\n{modified_content}")




