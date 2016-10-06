import nltk
from nltk.corpus import stopwords
from nltk.corpus.reader.tagged import TaggedCorpusReader

import corpus.general.keywords as general_keywords
import corpus.computerscience.keywords as comp_sci_keywords

stopwords = set(stopwords.words('english'))

gen_keywords = set(keyword.lower() for keyword in general_keywords.keywords)
comp_keywords = set(keyword.lower() for keyword in comp_sci_keywords.get_keywords())

tagged_reader = TaggedCorpusReader(root='/home/mo/projects/Nomad/data/analysis/corpus/computerscience/train/',
                                   fileids='.*')

