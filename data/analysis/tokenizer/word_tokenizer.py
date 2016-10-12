import re
import random

import nltk


def tokenize(summary, keywords):
    summary_sentences = summary.splitlines()

    sentences = []

    for sent in summary_sentences:
        parsed_sent = sent

        if sent:
            history = []

            for keyword_index, keyword in enumerate(keywords):

                keyword_pattern = re.compile(r'(?<=[\s(,-/])({})(?=[\s),-./])'.format(re.escape(keyword)), re.IGNORECASE)

                keyword_found = keyword_pattern.search(sent)

                if keyword_found:
                    keyword_hash = random.getrandbits(128)

                    parsed_sent = re.sub(keyword_pattern, r' {}_{} '.format(keyword_hash, keyword_index), parsed_sent)

                    history.append(('{}_{}'.format(keyword_hash, keyword_index), keyword_found.groups(0)[0]))

            # Tokenize after removing all potential keywords (otherwise, for example, C++ will be tokenized as C, +, +)
            sent_tokenized = nltk.word_tokenize(parsed_sent)

            for h in history:
                for i, token in enumerate(sent_tokenized):
                    if h[0] in token:
                        sent_tokenized[i] = token.replace(h[0], h[1])

            sentences.append(sent_tokenized)

    return sentences
