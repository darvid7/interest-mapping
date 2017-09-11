# Walkthrough on how the TensorFlow Word2Vec tutorial creates batch and label data sets.

- https://www.tensorflow.org/tutorials/word2vec
- https://github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/examples/tutorials/word2vec/word2vec_basic.py


```
- batch and labels are both numpy ndarray's.
- buf is a queue like object that sever's it's first element before appending one if it runs out of space (maxlen).

Example:

words = [
    "blue", "green", "violet","yellow", "orange",
    "orange", "is", "a", "fruit"
]

# Only look at first 3/4 items, UNK is the quarter we don't look at.
count = [
    ['UNK', 3], ('orange', 2), ('yellow', 1), ('is', 1), ('a', 1), ('blue', 1)
]
# index:  0   ,      1       ,      2       ,     3    ,    4    ,     5

dictionary = {
        'yellow': 2,
        'is': 3,
        'a': 4,
        'blue': 5,
        'orange': 1,
        'UNK': 0
}

reverse_dictionary = {
    2: 'yellow',
    3: 'is',
    4: 'a',
    5: 'blue',
    1: 'orange',
    0: 'UNK'
}

index:   0  1  2  3  4  5  6  7  8
data = [ 5, 0, 0, 2, 1, 1, 3, 4, 0 ]  # Can use the int value identify word using count or reverse dictionary


batch_size = 8
num_skips = 2
skip_window = 1
span = 3

buf.extend(data[data_index: data_index + span]) will populate the buffer fully.

buf = [5, 0, 0]
index =  0  1  2  3  4  5  6  7
batch = [0, ?, ?, ?, ?, ?, ?, ?]
label = [0, ?, ?, ?, ?, ?, ?, ?]

enter for loop i (8//2):

    # loop i iteration 1, i = 0.
    # data_index = 3
    target = skip_window = 1
    targets_to_avoid = [1]

    enter for loop j (2):

        # loop j iteration 1, j = 0.
        target = random target in range(0, span - 1) not in targets_to_avoid # between 0 and 2 inclusive.
        eg: target = 0
        add random target into targets_to_avoid, targets_to_avoid = [1, 0]
        batch[0 * 2 + 0]  = batch[0] = buf[1] = 0
        label[0 * 2 + 0] = label[0] = buf[target] = 5
        # batch and label now look like:
        # batch = [0, ?, ?, ?, ?, ?, ?, ?]
        # label = [5, ?, ?, ?, ?, ?, ?, ?]

        # loop j iteration 2, j = 1.
        target = random
        target = random target in range(0, span - 1) not in targets_to_avoid # between 0 and 2 inclusive.
        # can only pick 2 now.Â
        add random target into targets_to_avoid, targets_to_avoid = [1, 0, 2]
        batch[0 * 2 + 1] = batch[1] = buf[1] = 0
        label[0 * 2 + 1] = label[1] = buf[2] = 0
        # batch and label now look like:
        # batch = [0, 0, ?, ?, ?, ?, ?, ?]
        # label = [5, 0, ?, ?, ?, ?, ?, ?]

    exit loop j:
        buf.append(data[data_index]) = buf.append(data[3]) # buf becomes [0, 0, 2]
        data_index += 1

    # loop i iteration 2, i = 1.
    # data_index = 4        
    # buf = [0, 0, 2]
    target = skip_window = 1
    targets_to_avoid = [1]

    enter for loop j (2):

        # loop j iteration 1, j = 0.
        target = random target in range(0, span - 1)
        eg: target = 2
        add random target into targets_to_avoid, targets_to_avoid = [1, 2]
        batch[1 * 2 + 0] = batch[2] = buf[skip_window] = buf[1] = 0
        label[1 * 2 + 0] = label[2] = buf[target] = buf[2] = 2
        # batch and label now look like:
        # batch = [0, 0, 0, ?, ?, ?, ?, ?]
        # label = [5, 0, 2, ?, ?, ?, ?, ?]

        # loop j iteration 2, j = 1.
        target = random target in range(0, span - 1)
        can only pick target = 0
        add random target into targets_to_avoid, targets_to_avoid = [1, 2, 0]
        batch[1 * 2 + 1] = batch[3] = buf[skip_window] = buf[1] = 0
        label[1 * 2 + 1] = label[3] = buf[target] = buf[0] = 0
        # batch and label now look like:
        # batch = [0, 0, 0, 0, ?, ?, ?, ?]
        # label = [5, 0, 2, 0, ?, ?, ?, ?]

    exit loop j:
        buf.append(data[data_index]) = buf.append(data[4]) # buf becomes [0, 2, 1]
        data_index += 1

    # loop i iteration 3, i = 2.
    # data_index = 5
    # buf = [0, 2, 1]
    target = skip_window = 1
    targets_to_avoid = [1]

    enter for loop j (2):

        # loop j iteration 1, j = 0.
        target = random target in range(0, span - 1)
        eg: target = 0
        add random target into targets_to_avoid, targets_to_avoid = [1, 0]
        batch[2 * 2 + 0] = batch[4] = buf[skip_window] = buf[1] = 2
        label[2 * 2 + 0] = label[4] = buf[target] = buf[0] = 0
        # batch and label now look like:
        # batch = [0, 0, 0, 0, 2, ?, ?, ?]
        # label = [5, 0, 2, 0, 0, ?, ?, ?]

        # loop j iteration 2, j = 1.
        target = random target in range(0, span - 1)
        can only pick target = 2
        add random target into targets_to_avoid, targets_to_avoid = [1, 0, 2]
        batch[2 * 2 + 1] = batch[5] = buf[skip_window] = buf[1] = 2
        label[2 * 2 + 1] = label[5] = buf[target] = buf[2] = 1
        # batch and label now look like:
        # batch = [0, 0, 0, 0, 2, 2, ?, ?]
        # label = [5, 0, 2, 0, 0, 1, ?, ?]

    exit loop j:
        buf.append(data[data_index]) = buf.append(data[5]) # buf becomes [2, 1, 1]
        data_index += 1

    # loop i iteration 4, i = 3.
    # data_index = 6
    # buf = [2, 1, 1]
    target = skip_window = 1
    targets_to_avoid = [1]

    enter for loop j (2):

        # loop j iteration 1, j = 0.
        target = random target in range(0, span - 1)
        eg: target = 2
        add random target into targets_to_avoid, targets_to_avoid = [1, 2]
        batch[3 * 2 + 0] = batch[6] = buf[skip_window] = buf[1] = 1
        label[3 * 2 + 0] = label[6] = buf[target] = buf[2] = 1
        # batch and label now look like:
        # batch = [0, 0, 0, 0, 2, 2, 1, ?]
        # label = [5, 0, 2, 0, 0, 1, 1, ?]

        # loop j iteration 2, j = 1.
        target = random target in range(0, span - 1)
        can only pick target = 0
        add random target into targets_to_avoid, targets_to_avoid = [1, 2, 0]
        batch[3 * 2 + 1] = batch[7] = buf[skip_window] = buf[1] = 1
        label[3 * 2 + 1] = label[7] = buf[target] = buf[0] = 2
        # batch and label now look like:
        # batch = [0, 0, 0, 0, 2, 2, 1, 1]
        # label = [5, 0, 2, 0, 0, 1, 1, 2]

    exit loop j:
        buf.append(data[data_index]) = buf.append(data[6]) # buf becomes [1, 1, 3]
        data_index += 1

    # This is a global variable so will ensure we cover all data elements.
    data_index = (data_index  + len(data) - span) % len(data)
               = (7 + 8 - 3) % 8
               = 12 % 8
               = 4
    return batch, labels

    batch
    [0 0 0 0 2 2 1 1]

    labels
    [[5]
     [0]
     [2]
     [0]
     [0]
     [1]
     [1]
     [2]]
```
Great so now we know what goes on in `generate_batch()` but what is the relevance of `batch` and `label`.

`batch` are our context words, we can use `reverse_dictionary` to map this to words

`batch = ['UNK', 'UNK', 'UNK', 'UNK', 'yellow', 'yellow', 'orange', 'orange']`

`labels` are our targets (not it is a 2d numpy array, each element is a vector), likewise we can map this to words.

`labels = ['blue', 'UNK', 'yellow', 'UNK', 'UNK', 'orange', 'orange', 'yellow']`

```
words = [
    "blue", "green", "violet","yellow", "orange",
    "orange", "is", "a", "fruit"
]

# Only look at first 3/4 items, UNK is the quarter we don't look at.
count = [
    ['UNK', 3], ('orange', 2), ('yellow', 1), ('is', 1), ('a', 1), ('blue', 1)
]
```
Looking at our original text and count we can see that `'green', 'violet' and 'fruit'` is missing from count. This is because we only look at the first 3/4 words. So they are represented with UNK.

Pairing batch and labels results in:
```
[
#  (batch, target)
    ('UNK', 'blue'),  # probably ('green', 'blue')
    ('UNK', 'UNK'),   # probably ('violet', 'green')
    ('UNK', 'yellow'), # probably ('violet', 'yellow')
    ('UNK', 'UNK'),   # probably ('green', 'violet')
    ('yellow', 'UNK'), # probably ('yellow', 'violet')
    ('yellow', 'orange'),
    ('orange', 'orange'),
    ('orange', 'yellow')
]
```
We can see how it has generated (context, target) pairs to use for training using words on the left and right of the target word as expected.

As far as I know it is probably better to look at all words.
