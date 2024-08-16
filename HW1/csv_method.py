# ''''csv write''''
import csv

with open('employee_file.csv', mode='w',newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

# ''''csv read'''
# import csv

# with open('employee_birthday.txt', mode='r') as csv_file:
#     csv_reader = csv.DictReader(ç)
#     name_list = []
#     for row in csv_reader:
#         if row['birthday']==0101
#             name_list.append(rows['name])
# csv_file.close()    
