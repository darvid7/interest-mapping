# Interest Engine

The idea behind interest engine is to map a target interest to what comprises it/is related to it.

For example:

- the interest 'gaming' or 'gaming' might map to ['art', 'storyline', 'video', 'ux'] etc of things that make up a 'game'.
- the interest 'math' might map to ['finance', 'statistics', 'engineering', 'physics'] etc of things related to 'math'.

The mapping (embeddings created) dependent highly on your dataset.

This is a wip, at the moment we have a working Word2Vec model :smiley: :tada:

We have experimented with TensorFlow and gensim and have decided to use gensim because it is easier to implement.

## Installation

I recommend setting up a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to run this.

`pip3 install -r requirements.txt`

## Example Usage

```
usage: word_2_vec.py [-h] [-s SAVE_MODEL_PATH] [-q QUERY_WORDS_FILE_PATH]
                     [-v VERBOSE_VOCABULARY] [-mwc MINIMUM_WORD_COUNT]
                     [-sw SKIP_WINDOW]
                     training_data_file_path

Create and query a gensim word2vec model.

positional arguments:
  training_data_file_path
                        Path to training data

optional arguments:
  -h, --help            show this help message and exit
  -s SAVE_MODEL_PATH, --save_model_path SAVE_MODEL_PATH
                        Path to save Word2Vec model to. Default is
                        ./tmp/gensim_w2v.model
  -q QUERY_WORDS_FILE_PATH, --query_words_file_path QUERY_WORDS_FILE_PATH
                        Path to query words seperated by new line.
  -v VERBOSE_VOCABULARY, --verbose_vocabulary VERBOSE_VOCABULARY
                        Path to save vocabulary to so you can see what your
                        model is being trainned on.
  -mwc MINIMUM_WORD_COUNT, --minimum_word_count MINIMUM_WORD_COUNT
                        Minimum number of occurances of word for it to be
                        counted in model.
  -sw SKIP_WINDOW, --skip_window SKIP_WINDOW
                        Number of words either side of target to look.
```

For example:

`$ python3 word_2_vec.py example_input_data.txt -q example_query_file.txt`

Sample output:

```
words: 82780
Number of unique words: 7776
Training model
Saving model to tmp/gensim_w2v.model
Querying model
Nearest words to: pokemon
[('ruby', 0.9982284903526306), ('july', 0.998175859451294), ('duration', 0.9981691837310791), ('lana', 0.997929036617279), ('sep', 0.9979104995727539), ('veronica', 0.9976954460144043), ('talking', 0.9976745843887329), ('brains', 0.9976729154586792), ('network', 0.9976606965065002), ('jenny', 0.997484028339386)]
Nearest words to: yoda
[('dooku', 0.9875583648681641), ('darth', 0.9864420294761658), ('count', 0.9862101674079895), ('apprentice', 0.9822901487350464), ('maul', 0.9820522665977478), ('sidious', 0.9820424318313599), ('ahsoka', 0.9802110195159912), ('padawan', 0.9794387221336365), ('luke', 0.9792125225067139), ('ventress', 0.9780586957931519)]
Nearest words to: mace
[('luke', 0.9813833236694336), ('anakin', 0.9782136082649231), ('ahsoka', 0.9764122366905212), ('jinn', 0.9745883941650391), ('yoda', 0.9730238318443298), ('darth', 0.9724069237709045), ('qui', 0.9711713790893555), ('maul', 0.9709075093269348), ('vader', 0.9695415496826172), ('organa', 0.9671893119812012)]
Word lightsabre not in embeddngs.
Nearest words to: pikachu
[('used', 0.9704759120941162), ('lucario', 0.9623554944992065), ('started', 0.9600751996040344), ('air', 0.9589160680770874), ('double', 0.9562526345252991), ('thunderbolt', 0.9551534652709961), ('powerful', 0.9533454179763794), ('off', 0.9452481269836426), ('faced', 0.9442226886749268), ('metagross', 0.9429351091384888)]
Nearest words to: ash
[('pokémon', 0.9744959473609924), ('gym', 0.9366824626922607), ('first', 0.9309444427490234), ('faced', 0.925824761390686), ('battled', 0.9225589036941528), ('round', 0.9173986911773682), ('league', 0.9153050780296326), ('based', 0.9151893854141235), ('paul', 0.915047824382782), ('anime', 0.9147372841835022)]
Nearest words to: jedi
[('chancellor', 0.9836583137512207), ('side', 0.9819624423980713), ('dark', 0.9802864789962769), ('war', 0.9782619476318359), ('sith', 0.9777048230171204), ('lord', 0.9775424599647522), ('council', 0.9771016836166382), ('senate', 0.9758751392364502), ('order', 0.9731391072273254), ('separatist', 0.9688656330108643)]
```
## Explanation

The follow material has been taken from https://www.tensorflow.org/tutorials/word2vec in an effort to understand how Word2Vec works.

### Word Embeddings

Word embeddings is the name for NLP modeling & feature learning techniques where words/phrases are mapped to vectors of real numbers.

NLP systems usually treat words as discrete atomic symbols.

- 'cat' may be represented as `Id537`
- 'dog' may be represented as `Id143`

Encoding words as discrete atomic symbols doesn't provide useful information on the relationship between those individual symbols.

This results in models not being able to leverage what it has learnt about 'cats' when processing information about dogs.

Eg:
- 4 legged animal
- pets
- have tails

### Vector Space Models (VSM)

Represent (embed) words in continuous vector space where semantically similar words (words that mean similar things) are mapped to near by points (embedded nearby each other).

Depends on `Distributional Hypothesis` (words that appear in same contexts share semantic meaning).

Two categories of approaches depend on Distributional Hypothesis.

#### 1. Count-based methods (Latent Semantic Analysis)
Compute how often some word co-occurs with its neighbour words, map count statistics to a small dense vector for each word.

#### 2. Predictive methods (Neural Probabilistic Language models)
Try predict a word from its neighbours based on learn small dense embedding vectors (a model parameter).

Word2Vec is predictive.

### Word2Vec

Computation efficient predictive model for learning word embeddings from raw text.

2 versions:

#### 1. Continuous Bag-of-Words (CBOW)
CBOW predicts target words from source context words eg:

| context | predicted target |
| --- | --- |
| the cat sits on the | mat |
| an apple a day keeps the doctor | away |

Smoothes over a lot of distributional information by treating an entire context as one observation.
Useful for smaller data sets.

Any variation of bag-of-words models assume we can learn what a word means by looking at words that tend to appear near it.

CBOW trains each word against its context asking given a set of context words, what missing word is likely to appear at the same time?

#### 2. Skip-Gram model
Does opposite from CBOW. Predicts source context words from target words.

Skip-gram treats each context-target pair as a new observations and tends to do better with larger data sets.

Skip-Gram trains each context against the word, asking given this single word, what other words are likely to appear near it at the same time?

### Skip-Gram Word2Vec approach

#### 1. Dataset.

dataset = `the quick brown fox jumped over the lazy dog`

#### 2. Context

Context can be defined in any way that makes sense.

Syntactic contexts:
- Syntactic dependents (linguistics related)
- Words to left of target
- Words to right of target

Default: context is the window of words to the left and right of the target word (1 left and 1 right of target).

dataset = `(([the, brown] quick), ([quick, fox], brown), ([brown, jumped], fox)...)`

Formed of `([context], target_word)` pairs.

#### 3. Skip-Gram inverts contexts and targets.

Skip-Gram tries to predict each context word from it's target word.

So predict 'the' and 'brown' from the target 'quick'.

The dataset is transformed into `(input, output)` pairs.

dataset = `((quick, the), (quick, brown), (quick, brown), (fox, brown), (brown, fox), (jumped, fox)...)`

#### 4. Optimize objective function using gradient descent (approach min/max slowly incrementing)

1. An objective function is defined over the entire dataset.
2. This is optimized with stochastic gradient descent (SGD) one example at a time.

SDG is an incremental gradient descent, a stochastic approximation of gradient descent optimization to minimize objective function. Tries to find minima/maxima by iteration.

3. Training step

My high level understanding so far.
```
For each (target_word, context_prediction) pair sample.
    # eg: predict 'the' from 'quick'
    Select some noisy example (bad words)
        Compute Loss for pair & noisy example
            Update embeddings to maximise objective function
```

[How Word2Vec examples in TensorFlow generate batches and labels](https://github.com/darvid7/interest-engine/blob/master/Tensorflow_Generate_Batch.md)
