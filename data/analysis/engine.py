import os
import sys
import re
import cPickle as pickle

import filters

import chunker.chunk_tagger as chunk_tagger
import data.analysis.corpus.computerscience.keywords as comp_sci_keywords

sys.modules['chunker.chunk_tagger'] = chunk_tagger


def filter_summary(summary):
    # Certain jobs have special info about location of job
    location_info_patt = re.compile('(\*\*\*\sPLEASE NOTE:[\s\S]*?\*\*\*)')
    filtered_summary = re.sub(location_info_patt, '', summary)

    # Generate regex for each summary to be removed. Allows for multiple spaces and/or new lines between words.
    for text in filters.remove:
        text_patt_str = ['(']
        filtered_text = text.replace('.', '\.').replace('*', '\*').replace('(', '\(').replace(')', '\)')

        for word in filtered_text.split():
            text_patt_str.append(word + r'[\s|\n]*?')

        text_patt_str.append(')')
        text_patt = ''.join(text_patt_str)

        filtered_summary = re.sub(re.compile(text_patt), '', filtered_summary)

    # Remove asterisks
    filtered_summary = re.sub('[*]', '', filtered_summary)

    # Remove non-ascii characters
    filtered_summary = (re.sub(r'[^\x00-\x7F]+', '', filtered_summary)).strip()

    return filtered_summary


def get_keywords(summary, programs):
    for program in programs:
        if 'MATH' in program or 'ENG' in program:
            keywords = comp_sci_keywords.generate_keywords(summary)
            generated_keywords = load_chunker('computerscience').get_keywords(summary, keywords)

            for k in generated_keywords[:]:
                if k not in keywords:
                    generated_keywords.remove(k)

            return generated_keywords

    return []


def load_chunker(corpus_name):
    with open('{}/chunker/{}.pickle'.format(os.path.dirname(os.path.abspath(__file__)), corpus_name), 'rb') as f:
        return pickle.load(f)
