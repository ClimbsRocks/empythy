import csv


def load_dataset(file_name):

    with open(file_name, 'rU') as input_file:

        training_rows = csv.DictReader(input_file)

        return_data = []

        for row in training_rows:
            return_data.append(row)

        return return_data

def clean_initial_data(raw_data, confidence_threshold=None):

    corpus_strings = []
    sentiments = []
    for row in raw_data:
        if confidence_threshold is None or (row.get('confidence', 0) != '' and row.get('confidence', 0) > confidence_threshold):
            sentiments.append(row['sentiment'])
            corpus_strings.append(row['text'])

    return corpus_strings, sentiments