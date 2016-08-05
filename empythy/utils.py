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
    try:
        movie_reviews.categories()
    except:
        import nltk
        print('This appears to be your first time using the NLTK Movie Reviews corpus. We will first download the necessary corpus (this is a one-time download that might take a little while')
        nltk.download('movie_reviews')
        from nltk.corpus import movie_reviews

    raw_data = []

    # NLTK's corpus is structured in an interesting way
    # first iterate through the two categories (pos and neg)
    for category in movie_reviews.categories():

        if category == 'pos':
            pretty_category_name = 'positive'
        elif category == 'neg':
            pretty_category_name = 'negative'

        # each of these categories is just fileids, so grab those
        for fileid in movie_reviews.fileids(category):

            # then each review is a NLTK class where each item in that class instance is a word
            review_words = movie_reviews.words(fileid)
            review_text = ''

            for word in review_words:
                review_text += ' ' + word

            review_dictionary = {
                'text': review_text,
                'sentiment': pretty_category_name
            }

            raw_data.append(review_dictionary)

    return raw_data
