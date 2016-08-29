# empathyMachines
> A standalone NLP sentiment classifier you can import as a module

## Purposes

1. Offer a batteries-included NLP classifier you can use either on it's own, or to make sentiment predictions as part of a broder NLP project (for example, when classifying customer messages, whether the customer is angry or not might help you determine if this is a compensation request, or a request to adjust their address.)
1. Have the entire sentiment prediction process scaffolded so you can feed in your own training corpus, and easily train an NLP sentiment classifier.

## How to use

1. `pip install empythy`
1.
```
from empythy import EmpathyMachines
nlp_classifier = EmpathyMachines()
nlp_classifier.train()
nlp_classifier.predict(text_string)
```

### Corpora included

#### NLTK Movie Reviews
The classic sentiment corpus, 2000 movie reviews already gathered by NLTK.

#### Assembling a custom Twitter sentiment corpus
[CrowdFlower](http://www.crowdflower.com/data-for-everyone) hosts a number of Twitter corpora that have already been graded for sentiment by panels of humans.

I aggregated together 6 of their corpora into a single, aggregated and cleaned corpus, with consistent scoring labels across the entire corpus. The cleaned corpus contains over 45,000 documents, with positive, negative, and neutral sentiments.


### Train on your own corpus

Feel free to train a classifier on your own corpus!

Two ways to do this

1. Read in a .csv file with header row containing "sentiment", "text", and optionally, "confidence"
    - Pass the name of the .csv file to train, like so:
    - `nlp_classifier.train(corpus='custom', corpus_path='path/to/custom/corpus.csv')`
1. Pass in an array of Python dictionaries, where each dictionary has attributes for "sentiment", "text", and optionally, "confidence"
    - `nlp_classifier.train(corpus='custom', corpus_array=my_array_of_texts)`
    - Two important parts to this, both `corpus='custom'`, and `corpus_array=my_variable_holding_the_documents`.

### Advanced Usage
1. `nlp_classifier.train(verbose=False)` to turn off print status statements while training.
1. `nlp_classifier.train(print_analytics_results=True)` to print out results of training the classifier.
