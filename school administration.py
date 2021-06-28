import csv
import os
def file_found(file_path):
    #this function returns 
    return os.path.exists(file_path)

def write_into_csv1(info_list):
    #this function is for writing into csv with headers if file not created
    with open('student_info.csv','a',newline='') as csv_file:
            writer=csv.writer(csv_file)
            writer.writerow(['NAME','AGE','CONTACT NO','EMAIL ID'])
            writer.writerow(student_info_list)
            
def write_into_csv2(info_list):
    #this function for writing into csv file if file already exists
    with open('student_info.csv','a',newline='') as csv_file:
            writer=csv.writer(csv_file)
            writer.writerow(student_info_list)

condition=True
while(condition):
    student_info=input("Enter Student information in the following format(Name Age Contact_Number E-mail_ID):")
    print("Entered inforamtion: "+student_info)
    #funtion to s
    student_info_list=student_info.split(' ')

    #condition for writing data into csv file
    if file_found('student_info.csv')==True:
        print('file found')
        #funtion call
        write_into_csv2(student_info_list)
    else:
        #funtion call
        write_into_csv1(student_info_list)
        
    #user input for adding more student data
    while True:
        condition_check=input("Enter (yes/no) if you want to enter information for another student:")
        if condition_check=='yes':
            condition=True
            break
        elif condition_check=='no':
            condition=False
            break
        else:
            print('Invalid input! Please try again')
            continue
