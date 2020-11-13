The project takes a text file 'sentences.txt' consisting of some (>1) sentences and returns a text file 'sorted_sentences.txt' consisting of the same sentences sorted by their similarity to the first one. The similarity is calculated according to the cosine distance between the vectors representing a word structure of the sentences.
The program doesn't take into account the synonyms and even different forms of a word but still can be very useful to find similar sentences. In the given example it performs quite well and manages to distinguish different 'cats'.
