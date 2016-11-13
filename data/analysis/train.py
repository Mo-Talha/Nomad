import sys
import os

import nltk

from nltk.corpus import PlaintextCorpusReader

from chunker.chunk_tagger import Chunker

import data.analysis.tokenizer.word_tokenizer as tokenizer
import data.analysis.corpus.computerscience.keywords as comp_sci_keywords


def print_chunk_score(chunkscore):
    print chunkscore
    print ""

    print "Chunker missed sentences: "
    print chunkscore.missed()
    print ""

    print "Chunker incorrect sentences: "
    print chunkscore.incorrect()
    print ""


def parse_sentence(chunker, sent, keywords):
    tokenized_sentence = tokenizer.tokenize(sent, keywords)
    tagged_sentence = nltk.pos_tag(tokenized_sentence)

    return chunker.parse(tagged_sentence)


def train_computer_science(save):
    comp_sci_corpus = PlaintextCorpusReader('{}/corpus/computerscience/'
                                            .format(os.path.dirname(os.path.abspath(__file__))), '.*')

    comp_sci_chunker = Chunker('computerscience', comp_sci_corpus.raw('train.txt'))
    chunk_score = comp_sci_chunker.evaluate(comp_sci_corpus.raw('test.txt'))

    print_chunk_score(chunk_score)

    if save:
        comp_sci_chunker.save_chunker()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'comp-sci':
            train_computer_science(True)

    else:
        comp_sci_corpus = PlaintextCorpusReader('{}/corpus/computerscience/'
                                                .format(os.path.dirname(os.path.abspath(__file__))), '.*')

        comp_sci_chunker = Chunker('computerscience', comp_sci_corpus.raw('train.txt'))
        chunk_score = comp_sci_chunker.evaluate(comp_sci_corpus.raw('test.txt'))

        print_chunk_score(chunk_score)

        while True:
            try:

                sentence = raw_input("Please enter a sentence:\n")

                sentence_keywords = comp_sci_keywords.generate_keywords(sentence)

                print parse_sentence(comp_sci_chunker, sentence, sentence_keywords)

            except Exception as e:
                print e
