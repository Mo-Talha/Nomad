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

    if i < 505:
        continue

    summary = engine.filter_summary(job.summary).encode('ascii', 'ignore')

    summary_keywords = comp_sci_keywords.generate_keywords(summary)

    sentences = tokenizer.tokenize(summary, summary_keywords)
    sentences = [nltk.pos_tag(sent) for sent in sentences]

    for sentence in sentences:
        begin = False
        inside = False
        contains_keyword = False

        iob_tag = ''

        iob_tags = []

        for word in sentence:

            if word[0]:
                if word[0].lower() not in [keyword.lower() for keyword in summary_keywords]:
                    iob_tag = ' '.join(word + ('O', ))
                    begin = False
                    inside = False

                else:
                    begin = True
                    contains_keyword = True

                    if begin and not inside:
                        begin = False
                        inside = True
                        iob_tag = '{} {} B-KEYWORD'.format(*word)

                    elif inside:
                        iob_tag = '{} {} I-KEYWORD'.format(*word)

            if iob_tag:
                iob_tags.append(iob_tag)

        if contains_keyword:
            for iob in iob_tags:
                train_file.write(iob + "\n")

train_file.close()
