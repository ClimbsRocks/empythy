import csv


def load_dataset(file_name):

    with open(file_name, 'rU') as input_file:
    # detect the "dialect" of this type of csv file

    try:
        dialect = csv.Sniffer().sniff(input_file.read(1024))
    except:
        # if we fail to detect the dialect, defautl to Microsoft Excel
        dialect = 'excel'

    input_file.seek(0)
    training_rows = csv.DictReader(input_file, dialect)

    return_data = []

    for row in training_rows:
        return_data.append(row)

    return return_data
