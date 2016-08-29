import csv


def load_dataset(file_name):

    with open(file_name, 'rU', encoding='latin-1') as input_file:

        training_rows = csv.DictReader(input_file)

        return_data = []

        for row in training_rows:
            return_data.append(row)

        return return_data

# mostly functional, but not finished yet
# class NlpFeatureExtraction(BaseEstimator, TransformerMixin):

#     def __init__(self):
#         pass

#     def fit(self, X, y=None):
#         # implemented to be consistent with API requirements.
#         # this functionality doesn't actually require fitting to data at all, it's just a couple hardcoded heuristics
#         return self

#     def transform(self, X, y=None):

#         punctuation_counts = []
#         exclamation_point_counts = []
#         capital_letter_counts = []
#         # all_cap_word_counts = []
#         for text in X:
#             # rough pseudocode follows:

#             text_len = len(text)

#             punctuation_count = 0
#             exclamation_point_count = 0
#             capital_letter_count = 0

#             for char in text:
#                 if char in punctuation_set:
#                     punctuation_count += 1
#                     if char == '!':
#                         exclamation_point_count += 1
#                 elif char in capital_letter_set:
#                     capital_letter_count += 1
#             punctuation_counts.append(punctuation_count / text_len)
#             exclamation_point_counts.append(exclamation_point_count / text_len)
#             capital_letter_counts.append(capital_letter_count / text_len)

def clean_initial_data(raw_data, confidence_threshold=None):

    corpus_strings = []
    sentiments = []
    for row in raw_data:
        if confidence_threshold is None or (row.get('confidence', 0) != '' and float(row.get('confidence', 0)) > confidence_threshold):
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
