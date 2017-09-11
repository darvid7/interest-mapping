# Interest Engine

I recommend setting up a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to run this.

Explainations coming soon.

## Example Usage

```
usage: word_2_vec.py [-h] [-s SAVE_MODEL_PATH] [-q QUERY_WORDS_FILE_PATH]
                     training_data_file_path

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
