import os
import csv
from turtle import title

importantpath= os.path.join('..', 'Resources', 'netflix_ratings.csv')
Video_input = input("What video are you looking for? ")
with open (importantpath) as csvfile :
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # print(f"CSV header: {csv_header}")
    for row in csvreader:
        if Video_input == row[0] :
            print(f"{row[0]} has a rating of {row[1]} and a current rating of {row[5]}")
        else :
            print("The video you were looking for could not be found.")
            break
        
        # if Video_input != row[0] :
        #     print("The video you were looking for could not be found.")