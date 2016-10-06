import nltk

from mongoengine import *

import shared.secrets as secrets
from models.job import Job

import engine


connect(secrets.MONGO_DATABASE, host=secrets.MONGO_HOST, port=secrets.MONGO_PORT)


for i, job in enumerate(Job.objects(programs="MATH-Computer Science")):

    train_file = open('/home/mo/projects/Nomad/data/analysis/corpus/computerscience/train/train_{}.txt'.format(i), 'w+')

    summary = engine.filter_summary(job.summary).encode('ascii', 'ignore')

    sentences = summary.splitlines()

    sentences = [nltk.word_tokenize(sent) for sent in sentences]

    sentences = [nltk.pos_tag(sent) for sent in sentences]

    for sentence in sentences:
        train_sentence = ''

        for word in sentence:
            train_sentence += '{}./{} '.format(word[0], word[1])

        if train_sentence:
            train_file.write(train_sentence)
            train_file.write('\n')

    train_file.close()
