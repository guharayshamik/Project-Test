import csv, requests
import pandas as pd
import pandas.io.common


print("Qust 5: Write a python script to extract all usernames from the email addresses present in a given text file. Ex: username@domain.com. Display all user names, by sorting/ordering based on their domain names.")
print("Ans: ")

#Place a file in your C:\sample_input_path\user_email_lists.txt and pass the use email id lists.
try:
  reader = pd.read_csv('C:\\sample_input_path\\user_email_lists.txt', header=None)
  actual_list=reader[0].tolist()
except FileNotFoundError:
    print ("FILE_MISSING_MESSAGE: File named 'user_email_lists.txt' should be placed under C:\sample_input_path\ in your local")
    exit()
except pandas.errors.EmptyDataError:
    print("FILE_FORMAT_ISSUE: File is empty")
    exit()
try:
    #Using lambda and sorted
    rev_sorted_list = sorted(actual_list, key=lambda x: x.split('@')[1])
    print("-- Listed below are the usernames loaded from csv --")
    print(actual_list)
    print("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" Ans: List of Usernames Sorted Based On Domain Name  ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for name in rev_sorted_list:
        user_name = name.split('@')[0].strip(']').strip('[').strip('\'')
        print(user_name)
except IndexError:
    print ("FILE_VERIFICATION_FAILED: Pls verify the context of the file - > emailids in incorrect format")
except AttributeError:
    print ("FILE_VERIFICATION_FAILED")