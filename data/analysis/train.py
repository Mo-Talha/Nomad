import os

import nltk
from nltk.corpus import stopwords
from nltk.corpus.reader.tagged import TaggedCorpusReader

from chunker.chunk_tagger import ChunkTagger

import corpus.general.keywords as general_keywords
import corpus.computerscience.keywords as comp_sci_keywords

#os.environ['MEGAM'] = '/home/mo/Downloads/MEGAM/megam-64'

nltk.config_megam('/home/mo/Downloads/MEGAM/megam-64.opt')

stopwords = set(stopwords.words('english'))

gen_keywords = set(keyword.lower() for keyword in general_keywords.keywords)
comp_keywords = set(keyword.lower() for keyword in comp_sci_keywords.get_keywords())

comp_sci_train = '{}/corpus/computerscience/train/'.format(os.path.dirname(os.path.abspath(__file__)))

tagged_reader = TaggedCorpusReader(root=comp_sci_train, fileids='.*')

chunk_tagger = ChunkTagger(tagged_reader.tagged_sents())


while True:
    try:
        print str(chunk_tagger.tag(raw_input('Enter a sentence to analyze')))

    except Exception as e:
        print e
