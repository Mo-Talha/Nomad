import sys
import os

from nltk.corpus import PlaintextCorpusReader

from chunker.chunk_tagger import Chunker


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

        print chunker.evaluate(comp_sci_corpus.raw('test.txt'))
