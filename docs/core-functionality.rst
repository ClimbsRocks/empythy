Installation
=============

``pip install empythy``

Core Functionality
===================

A quick demonstration of what you're really here for: easily getting sentiment predictions.

::

  from empythy import EmpathyMachines
  nlp_classifier = EmpathyMachines()
  nlp_classifier.train()

  text_string = "I love machine learning! And bikes. And wearing fun party pants."
  nlp_classifier.predict(text_string)
  # returns ['positive']

  text_list = [
  "I'm annoyed by closed-minded people who try to keep others excluded from machine learning functionality.",
  "I effing love pho.",
  "Ummm, can you add some exclamation points to the end of that previous one??"
  "That smells awful.",
  "I love hiding lovely cards in your backpack to surprise you throughout the day."
  ]

  nlp_classifier.predict(text_list)
  # returns ['negative', 'positive', 'neutral', 'negative', 'positive']

Basic API Documentation
=========================

First, you must instantiate a new EmpathyMachines object. Convention is to save it into a variable called ``nlp_classifier``. The rest of these docs will assume that you have done exactly that (``nlp_classifier = EmpathyMachines()``). If you're headstrong enough to do it differently, we'll assume you're also smart enough to adjust your reading of these docs appropriately :)


.. py:class:: EmapthyMachines()

  Parameters
  -----------
  None


.. py:method:: train(corpus=Twitter)

  This method will train your nlp classifier. This must be done before trying to get predictions.

  :rtype: None. This simply trains the classifier to prepare it to make predictions.

  Included Corpora
  -----------------

  A description of corpora included with the module.



Additional Features
====================

These optional features are really only useful if you're already using the core functionality of empythy. If you haven't yet started, head back there and play around for a bit first before revisiting this page!

.. index:: source document, output document

.. py:method:: nlp_classifier.train(verbose=True, print_analytics_results=False)

    :param verbose: ``True`` by default, but you can set to ``False`` to squelch some of the pesky logging that mere mortals need for comfort while their machines learn empathy.
    :type verbose: boolean
    :param print_analytics_results: For those who never could stop asking questions. Prints some of the results from training the model. Super useful if you're training on your own data and you want to get a good handle on how close your machine is to passing the Turing Test.
    :type print_analytics_results: boolean
