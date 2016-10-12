import sys
import os

from nltk.corpus import PlaintextCorpusReader

from chunker.chunk_tagger import Chunker

import data.analysis.tokenizer.word_tokenizer as tokenizer
import data.analysis.corpus.computerscience.keywords as comp_sci_keywords
import nltk


def print_chunk_score(chunkscore):
    print chunkscore
    print ""

    print "Chunker missed sentences: "
    print chunkscore.missed()
    print ""

    print "Chunker incorrect sentences: "
    print chunkscore.incorrect()
    print ""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'comp-sci':
            comp_sci_corpus = PlaintextCorpusReader('{}/corpus/computerscience/'
                                                    .format(os.path.dirname(os.path.abspath(__file__))), '.*')

            chunker = Chunker(comp_sci_corpus.raw('train.txt'))
            print chunker.evaluate(comp_sci_corpus.raw('test.txt'))

    else:
        comp_sci_corpus = PlaintextCorpusReader('{}/corpus/computerscience/'
                                                .format(os.path.dirname(os.path.abspath(__file__))), '.*')

        chunker = Chunker(comp_sci_corpus.raw('train.txt'))

        chunk_score = chunker.evaluate(comp_sci_corpus.raw('test.txt'))

        print_chunk_score(chunk_score)

        while True:
            try:

                sentence = raw_input("Please enter a sentence:\n")

                sentence_keywords = comp_sci_keywords.generate_keywords(sentence)

                tokenized_sentence = tokenizer.tokenize(sentence, sentence_keywords)

                tagged_sentence = nltk.pos_tag(tokenized_sentence[0])  # Get first sentence

                print chunker.parse(tagged_sentence)

            except Exception as e:
                print e
