# Explanation of how it works

https://www.tensorflow.org/tutorials/word2vec

## Word Embeddings

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

Any variation of bag-of-wrods models assume we can learn what a word means by looking at words that tend to appear near it.

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

daataset = `((quick, the), (quick, brown), (quick, brown), (fox, brown), (brown, fox), (jumped, fox)...)`

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
