
import csv
import os


def read_bestsellers():
    data_full_path = os.environ['DATA_PATH'] + "/" + \
        os.environ['NETFLIX_DATA_PATH']
    with open(data_full_path) as csv_file:
        reader = csv.reader(csv_file)
        return list(reader)
