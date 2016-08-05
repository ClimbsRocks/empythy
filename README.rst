# empathyMachines
> A standalone NLP sentiment classifier you can import as a module

## Purposes

1. Offer a batteries-included NLP classifier you can use either on it's own, or to make sentiment predictions as part of a broder NLP project (for example, when classifying customer messages, whether the customer is angry or not might help you determine if this is a compensation request, or a request to adjust their address.)
1. Have the entire sentiment prediction process scaffolded so you can feed in your own training corpus, and easily train an NLP sentiment classifier.

## How to use

1. Download the repo from GitHub (pip install coming later)
1. `cd` into repo, and `pip install -r requirements.txt`
1. In your Python code, `from EmpathyMachines import EmpathyMachines`
1. `nlp_classifier = EmpathyMachines()`
1. `nlp_classifier.train(corpus='Twitter')`
1. `nlp_classifier.predict(text_string)`


### Corpora included


### Include your own corpus (UNDER CONSTRUCTION)

Feel free to train a classifier on your own corpus!

Two ways to do this:
1. Read in a .csv file with header row containing "sentiment", "text", and optionally, "confidence"
1. Pass in an array of Python dictionaries, with attributes for "sentiment", "text", and optionally, "confidence"


1. Create a .csv file with the following fields
1. `nlp_classifier.train(corpus='custom', corpus_path='path/to/custom/corpus.csv', analytics_output=False)`
