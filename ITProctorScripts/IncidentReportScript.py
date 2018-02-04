from datetime import datetime
import os


IT_PROCTOR = 'Arash Outadi'
TODAY_DATE = str(datetime.today().date())
MODULE = 'PREP'
EXT = r'.txt'
DIRECTORY = r'C:\Users\arash\Desktop'

time_occurrence = 'Time of Occurrence: ' + \
                  input('Time issue occured:\n') + '\n'
canadiate_name = 'Candidate Name: ' + \
                 input('Enter the canadiate name:\n') + '\n'
canadiate_id = 'Canadiate ID: ' + \
               input('Enter the canadiate ID:\n') + '\n'
issue = 'Issue: ' + \
        input('Describe the issue:\n') + '\n'
solution = 'Solution: ' + \
           input('Describe the solution:\n') + '\n\n'


incident_report_file_name = 'Incident_Report_' + TODAY_DATE + EXT
incident_report_file_path = os.path.join(DIRECTORY, incident_report_file_name)

with open(incident_report_file_path, 'a') as f:
    content = time_occurrence + canadiate_name + \
        canadiate_id + issue + solution
    f.write(content)

