import csv
from typing import List
import time

import requests

#csv_file_name = input("Enter path to CSV, which contains IP Addresses:\n")
csv_file_name = "ipAddresses.csv"

new_csv_name = "ipInfo.csv"

# Assume:
# First 3 columns are occupied with information

api_url = r"http://ip-api.com/csv/"
requests_limit = 100
requests_throttle_time = 60  # Seconds

new_csv_content: List[str] = []

with open(csv_file_name, 'r') as csvfile:
    reader: csv.reader = csv.reader(csvfile, delimiter=',')

    i: int = 0
    start_row = 1339

    row: List[str]
    for row in reader:
        i += 1
        # Skip the header and any rows already read
        if i <= start_row:
            continue

        # IP address in 2nd column
        ip_address: str = row[1]

        # To avoid getting IP banned, need the program to sleep occasionally
        if i % requests_limit == 0:
            print("Appending information to file\nEnd at row: {0}".format(i))
            with open(new_csv_name, "a", encoding="utf-8") as f:
                f.writelines(new_csv_content)

            # Append results to new CSV file
            time.sleep(requests_throttle_time)



            new_csv_content.clear()

        response: requests.Response = requests.get(api_url + ip_address)

        if response.status_code == 200:
            # Response is in CSV format
            # Concanate first 3 columns with response text and a newline
            new_csv_content.append(",".join(row[0:3]) + "," + response.text + '\n')


