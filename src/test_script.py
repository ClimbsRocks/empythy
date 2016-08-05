from EmpathyMachines import EmpathyMachines

nlp_classifer = EmpathyMachines()

nlp_classifer.train(print_analytics_results=True, corpus='Twitter')


test_strings = ['i hate this new sugary cereal','i hate this new sugary cereal : (','i love this awesome new machine learning library!','TfidfVectorizer is definitely not contained in scikit-learn\'s stopwords corpus']

for text in test_strings:
    print(nlp_classifer.predict(text))

print(nlp_classifer.predict(test_strings))
