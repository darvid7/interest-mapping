import argparse
import gensim
import os

from gensim.models import Word2Vec

print("Loading pre-trained model")
model = Word2Vec.load('tmp/future_you.model')

query_words = [
    ['accountant', 'math'],
    ['mental', 'health'],
    ['lawyer', 'law'],
    ['programmer', 'computer'],
    ['author', 'math']
]

print('---- Finding near by words for singular word ----')
for query_list in query_words:
    for single_word in query_list:
        try:
            print("Nearest words to: {0}\n{1}".format(
                single_word, model.wv.most_similar(positive=single_word)))
        except KeyError:
            print("Word {0} not in embeddngs.".format(single_word))


print('---- Finding near by words for word pairs ----')
for query_list in query_words:
    try:
        print("Nearest words to: {0}\n{1}".format(
            query_list, model.wv.most_similar(positive=query_list)))
    except KeyError:
        print("Word {0} not in embeddngs.".format(query_list))

print('--- Similarity ----')
for query_list in query_words:
    try:
        print("Similarty between word {0} is {1}".format(
            query_list, model.wv.similarity(query_list[0], query_list[1])
        ))
    except KeyError as ex:
        print("Error finding similarity for words {0}. Error: {1}".format(query_list, ex))
