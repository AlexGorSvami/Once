res = {}

from pprint import pprint
text = """
Говорят, ее забыли
Говорят, ее не ждут
Говорят, другие звезды
Светят ярче и поют
А она брошена в испуге.
"""
split_text = text.lower().split()

for word in split_text:
    word = word.strip(',./!?')
    res.setdefault(word, 0)
    res[word] += 1

pprint(res)
print(dict(sorted(res.items(), key=lambda kv: kv[1])))
