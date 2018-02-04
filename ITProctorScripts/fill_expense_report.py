from fdfgen import forge_fdf
from datetime import datetime
import os

#Default Fields
rate = 50
fields = [
    ('Name','Arash Outadi'),
    ('Phone','778-987-8654'),
    ('Rate',str(rate)),
    ('PayTo','Arash Outadi'),
    ('Address','4380 Halifax Street, Suite 1405'),
    ('CityProvince','Burnaby, BC'),
    ('PostalCode','V5C 6R3')
    ]

#Dynamic Fields
event_field = ("Event", input("Event (PREP/PEP):\n"))
location_field = ("Location", input("Location:\n"))
dates_field = ("Dates", input("Exam Dates:\n"))
date_field = ("Date", datetime.now().date())
hours = float(input("Hours Worked:\n"))
hours_field = ("Hours", hours)
net_amount_field = ("NetAmount", float(hours * rate))
total_expenses_field = ("TotalExpenses", float(hours * rate))

#Extending the list of tuples that contains the fields
fields.extend([
    event_field,
    location_field,
    dates_field,
    date_field,
    hours_field,
    total_expenses_field,
    net_amount_field
    ])


fdf = forge_fdf("",fields,[],[],[])
#Create a fdf file that you read with pdftk
fdf_file_name = "data.fdf"
fdf_file = open(fdf_file_name,"wb")
fdf_file.write(fdf)
fdf_file.close()
#Use CMD to execute command to create pdf
exam_dates = dates_field[1].replace(' ','_')
command = 'pdftk BlankExpense.pdf fill_form data.fdf output ExpenseReport_{0}.pdf flatten'.format(exam_dates)
os.system(command)

os.remove(fdf_file_name)
