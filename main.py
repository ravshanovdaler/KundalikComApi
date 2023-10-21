import pandas as pd

excel = 'students.xlsx'

rf = pd.read_excel(excel, usecols=['first name', 'date of birth', 'last name', 'phone number', 'adress'])

first_name = rf['first name']


for student in first_name:
    print(student)