
import csv
from csv import DictReader
# leemos el archivo y lo guardamos en lista type Dict
def read(path):
    with open(path, "r+")as  file_csv:
        read = csv.DictReader(file_csv, delimiter = ",")
        list = []
        for data in  read:
            list.append(data)
        return list


if __name__ == "__main__":
    read("./date.csv")