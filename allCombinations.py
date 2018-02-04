import csv
import itertools
import sys

if len(sys.argv) < 2:
    raise Exception('You need to pass a filepath!')

FILE_PATH = sys.argv[1]

def read_csv(file_path: str) -> list:
    with open(file_path) as csvfile:
        # Skip first line which is header
        next(csvfile)

        rows = csv.reader(csvfile, delimiter=',')
        # Get list of lists, where inner lists are columns
        res = list(itertools.zip_longest(*rows))
        # Filter out Nones
        filtered_lists = [list(filter(''.__ne__, l)) for l in res]

    return filtered_lists

def write_csv(file_path: str, nested_list: list):
    with open(file_path, "w") as f:
        writer = csv.writer(f)
        writer.writerows(nested_list)

if __name__ == '__main__':
    list_of_lists = read_csv(FILE_PATH)
    write_csv('output.csv', itertools.product(*list_of_lists))