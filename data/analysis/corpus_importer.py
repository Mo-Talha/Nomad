import nltk

import corpus.computerscience.keywords as comp_sci_keywords
import tokenizer.word_tokenizer as tokenizer

from mongoengine import *

from models.job import Job

import shared.secrets as secrets
import engine


connect(secrets.MONGO_DATABASE, host=secrets.MONGO_HOST, port=secrets.MONGO_PORT)

train_file = open('/home/mo/projects/Nomad/data/analysis/corpus/computerscience/train.txt', 'w+')

comp_keywords = set(comp_sci_keywords.get_keywords())

for i, job in enumerate(Job.objects(programs="MATH-Computer Science")):

    if i < 500:
        continue

    summary = engine.filter_summary(job.summary).encode('ascii', 'ignore')

    summary_keywords = comp_sci_keywords.generate_keywords(summary)

    sentences = tokenizer.tokenize(summary, summary_keywords)
    sentences = [nltk.pos_tag(sent) for sent in sentences]

    for sentence in sentences:
        begin = False
        inside = False
        iob_tag = ''

        for word in sentence:

            if word[0]:
                if word[0].lower() not in [keyword.lower() for keyword in summary_keywords]:
                    iob_tag = ' '.join(word + ('O', ))
                    begin = False
                    inside = False

                else:
                    begin = True

                    if begin and not inside:
                        begin = False
                        inside = True
                        iob_tag = '{} {} B-KEYWORD'.format(*word)

                    elif inside:
                        iob_tag = '{} {} I-KEYWORD'.format(*word)

            if iob_tag:
                train_file.write(iob_tag + "\n")

train_file.close()
