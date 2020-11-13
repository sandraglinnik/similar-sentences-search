import re
import numpy as np
from scipy.spatial.distance import cosine


with open('sentences.txt', 'r') as f:
    original_sentences = f.readlines()

sentences = []
for s in original_sentences:
    sentences.append(list(filter(lambda w: w not in {'', 'the', 'a'}, re.split('[^a-z]', s.lower()))))

word_id = {}
word_count = 0
for s in sentences:
    for word in s:
        if word not in word_id.keys():
            word_id[word] = word_count
            word_count += 1

n = len(sentences)
m = len(word_id)
a = np.zeros((n, m))

for i in range(n):
    for w in sentences[i]:
        a[i, word_id[w]] += 1  # a[i, j] is count of word word_id[j] in sentences[i]

sorted_indexes = sorted(list(range(n)), key=lambda i: cosine(a[0], a[i]))  # sort sentences by similarity with the first one
ans = [original_sentences[i] for i in sorted_indexes]
with open('similar_sentences.txt', 'w') as f:
    print(*ans, file=f)

