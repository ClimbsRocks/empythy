Installation
=============

``pip install empythy``

Core Functionality
===================

A quick demonstration of what you're really here for: easily getting sentiment predictions.

::

  from empythy import EmpathyMachines
  sentiment_classifier = EmpathyMachines()
  sentiment_classifier.train()

  text_string = "I love machine learning! And bikes. And wearing fun party pants."
  sentiment_classifier.predict(text_string)
  # returns ['positive']

  text_list = [
    "I effing love pho.",
    "Ummm, can you add some exclamation points to the end of that previous one??"
    "I love hiding lovely cards in your backpack to surprise you throughout the day."
  ]

  sentiment_classifier.predict(text_list)
  # returns ['positive', 'neutral', 'positive']

Basic API Documentation
=========================

First, you must instantiate a new EmpathyMachines object. Convention is to save it into a variable called ``sentiment_classifier``. The rest of these docs will assume that you have done exactly that (``sentiment_classifier = EmpathyMachines()``). If you're headstrong enough to do it differently, we'll assume you're also smart enough to adjust your reading of these docs appropriately :)


.. py:class:: EmapthyMachines()

  :param: None. Literally, as in, don't pass in any arguments when creating a new EmpathyMachines instance.


.. py:method:: sentiment_classifier.train(corpus=Twitter)

  This method will train your nlp classifier. This must be done before trying to get predictions.

  :rtype: None. This simply trains the classifier to prepare it to make predictions.
  :param corpus: Which corpus of documents you want to train this model on. Currently, empythy ships with two corpora (Twitter, MovieReviews), along with the ability to pass in your own corpus to train on! If you're interested in getting fancy, instructions on how to train on your own custom dataset are later in this doc.
  :type corpus: string

  The included corpora are:

    * ``Twitter``

      [CrowdFlower](http://www.crowdflower.com/data-for-everyone) hosts a number of Twitter corpora that have already been graded for sentiment by panels of humans. I aggregated together 6 of their corpora into a single, aggregated and cleaned corpus, with consistent scoring labels across the entire corpus. The cleaned corpus contains over 45,000 documents, with positive, negative, and neutral sentiments, along with a score of how confident they are in that assessment.

    * ``MovieReviews``

      The classic NLTK corpus of movie reviews.




Additional Features
====================

These optional features are really only useful if you're already using the core functionality of empythy. If you haven't yet started, head back there and play around for a bit first before revisiting this page!

.. index:: source document, output document

.. py:method:: sentiment_classifier.train(verbose=True, print_analytics_results=False)

    :param verbose: ``True`` by default, but you can set to ``False`` to squelch some of the pesky logging that mere mortals need for comfort while their machines learn empathy.
    :type verbose: boolean
    :param print_analytics_results: For those who never could stop asking questions. Prints some of the results from training the model. Super useful if you're training on your own data and you want to get a good handle on how close your machine is to passing the Turing Test.
    :type print_analytics_results: boolean
