import cv2
import pandas as pd
from csv import reader


with open('E:/FYP/data.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        print(row)
