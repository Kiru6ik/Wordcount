import string
import re
import nltk
from nltk import word_tokenize
import csv
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

spec_chars = string.punctuation + "«»\t—…’"

f = open('/Users/kirillevseev/Downloads/Книга на перевод.txt', "r", encoding="utf-8")

text = f.read()
text = text.lower()
text = re.sub(r'http\S+', '', text)
text = re.sub('isbn', '', text)
text = re.sub('©', '', text)
text = "".join([ch for ch in text if ch not in spec_chars])
text = re.sub('\n', ' ', text)
text = "".join([ch for ch in text if ch not in string.digits])

text_tokens = word_tokenize(text)
text = nltk.Text(text_tokens)
stopwords=stopwords.words("english")
stopwords.extend(['–', '•'])
text_tokens = [token.strip() for token in text_tokens if token not in stopwords]
text = nltk.Text(text_tokens)

fdist = FreqDist(text)
# only_once=FreqDist.hapaxes(text_tokens)
words=fdist.most_common()
with open('dads_words.csv', 'w', encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerows(words)
