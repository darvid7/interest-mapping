import argparse
import gensim
import os

from gensim.models import word2vec

parser = argparse.ArgumentParser(description="Create and query a gensim " \
                                    "word2vec model.")

# Positional arguments (required).
parser.add_argument("training_data_file_path", type=str,
                    help="Path to training data")

# Optional arguments.
parser.add_argument("-s", "--save_model_path", type=str,
                    help="Path to save Word2Vec model to. Default is" \
                    " ./tmp/gensim_w2v.model",
                    default="tmp/gensim_w2v.model")

parser.add_argument("-q", "--query_words_file_path", type=str,
                    help="Path to query words seperated by new line.",
                    default=None)

args = parser.parse_args()


# TODO: Maybe check ascii bounds instead.
PARSE_OUT = {
    '/', ':', '-', '.', '\'', '–',
     "\t", "\"", ":", ",", "\\", "]", ";",
    "[", "{", "}", ".", '(', ')', '&', "!", "•", "―", "*"
}

def replace_with_dict_comprehension(string):
    """Replaces any character found in string matching a character in PARSE_OUT
    with a space ' ' so the data set is not skewed by punctation/formatting.
    """
    translation = string.translate({ord(c): ' ' for c in PARSE_OUT})
    return translation # Single string.


def read_text_data_as_sentences(filename):
    """Reads filename and returns the sentences in it after removing formatting.

    Returns:
        A list of sentences, each sentence is a list of words.
    """
    with open(filename, 'r') as fh:
        file_contents_as_string = fh.read()
        file_contents_as_string = replace_with_dict_comprehension(
                                    file_contents_as_string)
        sentences = file_contents_as_string.split('\n')
        parsed_sentences = []
        del file_contents_as_string
        # Parse out whitespace and digits.
        for sentence in sentences:
            sentence = [word.lower() for word in sentence.split(' ')
                            if word != "" and not word.isdigit()]
            if sentence:
                parsed_sentences.append(sentence)
        del sentences
        return parsed_sentences


def flatten_sentences_to_words(sentences):
    """Helper function to look get all words in a single list, not actually
    needed.
    """
    words = []
    for sentence in sentences:
        for word in sentence:
            words.append(word)
    return words

vocabulary_as_sentences = read_text_data_as_sentences(
                            args.training_data_file_path)

# Can remove to save time and space.
vocabulary = flatten_sentences_to_words(vocabulary_as_sentences)
print("Total number of words: " + str(len(vocabulary)))
print("Number of unique words: {0}".format(len(set(vocabulary))))
del vocabulary

print("Training model")
# Train word2vec on sentences.
# Note: sentences can be an iterator (use yeild).
model = gensim.models.Word2Vec(
    sentences=vocabulary_as_sentences,
    min_count=4,  # Min frequency needed to count word.
    workers=6,  # Threads.
    window=5,   # Window of words to left and right to consider.
    sg=1  # Use Skip-Gram not Continous Bag of Words.
)

print("Saving model to {0}".format(args.save_model_path))

if not os.path.isdir(os.path.dirname(args.save_model_path)):
    os.mkdir(os.path.dirname(args.save_model_path))

model.save(args.save_model_path)

# Query.
if args.query_words_file_path:
    print("Querying model")
    with open(args.query_words_file_path, "r") as fh:
        query_words = [word.strip().lower() for word in fh.readlines()]
        for query in query_words:
            try:
                print("Nearest words to: {0}\n{1}".format(
                    query, model.wv.most_similar(positive=[query])))
            except KeyError:
                print("Word {0} not in embeddngs.".format(query))
