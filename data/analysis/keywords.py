import nltk
from nltk.corpus import stopwords

import engine

from mongoengine import *

from models.job import Job

import shared.secrets as secrets
import data.analysis.raw.computerscience.keywords as comp_sci_keywords

connect(secrets.MONGO_DATABASE, host=secrets.MONGO_HOST,
        port=secrets.MONGO_PORT)

train_file = open('train_1.txt', 'w')

pattern = r"""
    NP:
        {<>}
"""

cp = nltk.RegexpParser(pattern)

stopwords = set(stopwords.words('english'))

for job in Job.objects(programs="MATH-Computer Science"):
    summary = engine.filter_summary(job.summary).encode('ascii', 'ignore')

    # Sentence tokenize
    sentences = summary.splitlines()

    # Remove stop words and word tokenize
    filtered_sentences = []

    for sentence in sentences:

        # Word tokenize
        filtered_sentences.append([word for word in nltk.word_tokenize(sentence) if word not in stopwords])

    # Add POS tags to filtered sentences
    sentences = [nltk.pos_tag(sent) for sent in filtered_sentences]

    for sentence in sentences:
        for word in sentence:
            if word[0].lower() in set(keyword.lower() for keyword in comp_sci_keywords.keywords):
                print sentence
