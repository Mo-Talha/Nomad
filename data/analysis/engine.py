import os
import sys
import re
import cPickle as pickle

import data.analysis.filters as filters

import data.analysis.chunker.chunk_tagger as chunk_tagger
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

            gen_keywords = []

            for k in generated_keywords:
                gen_keywords = parse_keywords(k, comp_sci_keywords.keywords, gen_keywords)

            return gen_keywords

    return []


def parse_keywords(key, keywords, gen_keywords):

    if not any(gk['keyword'] == key for gk in gen_keywords):
        keyword_dict = keywords[key]

        keyword = keyword_dict['keyword']
        types = [keyword_dict['type']]

        # Combine all types and extra types into one field
        if 'type_extra' in keyword_dict:
            types = types + keyword_dict['type_extra']

        gen_keywords.append({
            'keyword': keyword,
            'types': types
        })

        if 'extra' in keyword_dict:
            for k in keyword_dict['extra']:
                    gen_keywords = parse_keywords(k, keywords, gen_keywords)

    return gen_keywords


def load_chunker(corpus_name):
    with open('{}/chunker/{}.pickle'.format(os.path.dirname(os.path.abspath(__file__)), corpus_name), 'rb') as f:
        return pickle.load(f)
