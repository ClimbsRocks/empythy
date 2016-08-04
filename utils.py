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


def load_movie_reviews():

    # movie_reviews is a sizeable corpus to import, so only load it if we have to
    from nltk.corpus import movie_reviews

    raw_data = []

    for category in movie_reviews.categories():
        if category == 'pos':
            pretty_category_name = 'positive'
        elif category == 'neg':
            pretty_category_name = 'negative'
        else:
            print(category)
            continue

        for fileid in movie_reviews.fileids(category):
            review_dictionary = {
                'text': movie_reviews.words(fileid),
                'sentiment':pretty_category_name
            }

    return raw_data
