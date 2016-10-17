import os
import cPickle as pickle

import nltk
from nltk.tree import Tree

import data.analysis.tokenizer.word_tokenizer as tokenizer


class ChunkTagger(nltk.TaggerI):
    def __init__(self, train_sentences):
        nltk.config_megam('{}/../algorithms/megam-64.opt'.format(os.path.dirname(os.path.abspath(__file__))))

        train_set = []

        # train_sentences as: [[(('Confidence', 'NN'), 'B-NP'), (('in', 'IN'), 'O')..], ..]
        for tagged_sent in train_sentences:

            # untagged_sent: [(u'Experience', u'NN')]
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []

            for i, (word, tag) in enumerate(tagged_sent):
                feature_set = self.chunk_features(untagged_sent, i, history)
                train_set.append((feature_set, tag))
                history.append(tag)

        self.classifier = nltk.MaxentClassifier.train(train_set, algorithm='megam', trace=0)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            feature_set = self.chunk_features(sentence, i, history)
            tag = self.classifier.classify(feature_set)
            history.append(tag)
        return zip(sentence, history)

    @staticmethod
    def chunk_features(sentence, i, history):
        word, pos = sentence[i]

        if i == 0:
            prev_word, prev_pos, prev_pos_2nd = "<START>", "<START>", "<START>"
        else:

            if i == 1:
                prev_word_2nd, prev_pos_2nd = "<START>", "<START>"
                prev_word, prev_pos = sentence[i - 1]
            else:
                prev_word_2nd, prev_pos_2nd = sentence[i - 2]
                prev_word, prev_pos = sentence[i - 1]

        if i == len(sentence) - 1:
            next_word, next_pos, next_pos_2nd = "<END>", "<END>", "<END>"
        else:

            if i == len(sentence) - 2:
                next_word_2nd, next_pos_2nd = "<END>", "<END>"
                next_word, next_pos = sentence[i + 1]
            else:
                next_word_2nd, next_pos_2nd = sentence[i + 2]
                next_word, next_pos = sentence[i + 1]

        """
        Learning techniques: Keywords are likely to be NNP or NN (less likely).
        Keywords are likely to be bundled together.
        """

        return {
            "pos": pos,
            "prevpos": prev_pos,
            "nextpos": next_pos,
            "2ndprevpos": prev_pos_2nd,
            "2ndnextpos": next_pos_2nd,
            "prevpos+pos": "%s+%s" % (prev_pos, pos),
            "pos+nextpos": "%s+%s" % (pos, next_pos)
        }


class Chunker(nltk.ChunkParserI):
    def __init__(self, corpus_name, train_sentences):
        self.corpus_name = corpus_name

        # train_sents: [[u'Experience NN O', u'with IN O', u'application NN O', ..]]
        train_sents = [sentence.strip('\n').split('\n') for sentence in train_sentences.split('. . O')]

        # Generates tagged sentences as: [[(('Confidence', 'NN'), 'B-NP'), (('in', 'IN'), 'O')..], ..]
        tagged_sentences = [[self.iob2chunkertags(line) for line in sent] for sent in train_sents]

        self.tagger = ChunkTagger(tagged_sentences)

    def parse(self, sentence):
        tagged_sentence = self.tagger.tag(sentence)

        sentence_tags = [(word, tag, chunk_type) for ((word, tag), chunk_type) in tagged_sentence]

        return self.tags2tree(sentence_tags)

    def get_keywords(self, summary, corpus_keywords):
        keywords = []

        summary_sentences = [sentence.strip() for sentence in nltk.sent_tokenize(summary)]
        corpus_keywords_lower = [k.lower() for k in corpus_keywords]

        for sentence in summary_sentences:
            tokenized_sentence = tokenizer.tokenize(sentence, corpus_keywords)
            tagged_sentence = nltk.pos_tag(tokenized_sentence)

            conll_tree = self.parse(tagged_sentence)

            sentence_tags = nltk.chunk.tree2conlltags(conll_tree)

            for (word, tag, iob) in sentence_tags:
                if iob.endswith("KEYWORD") and word.lower() in corpus_keywords_lower:
                    keywords.append(corpus_keywords[corpus_keywords_lower.index(word.lower())])

        return list(set(keywords))

    def evaluate(self, test_sentences):
        test_sents = [sentence.strip('\n').split('\n') for sentence in test_sentences.split('. . O')]

        tagged_sentences = [[Chunker.iob2tags(line) for line in sent] for sent in test_sents]

        trees = []

        for sentence in tagged_sentences:
            tree = self.tags2tree(sentence)
            trees.append(tree)

        chunk_score = super(Chunker, self).evaluate(trees)

        return chunk_score

    def save_chunker(self):
        with open('{}/{}.pickle'.format(os.path.dirname(os.path.abspath(__file__)), self.corpus_name), 'wb') as f:
            pickle.dump(self, f)
            f.close()

    @staticmethod
    def iob2chunkertags(line):
        word, tag, chunk = line.rsplit(" ", 2)
        return (word, tag), chunk

    @staticmethod
    def iob2tags(line):
        word, tag, chunk = line.rsplit(" ", 2)
        return word, tag, chunk

    @staticmethod
    def tags2tree(sentence, root_label='S', strict=False):
        tree = Tree(root_label, [])
        for (word, postag, chunktag) in sentence:
            if chunktag is None:
                if strict:
                    raise ValueError("Bad tag sequence")
                else:
                    # Treat as O
                    tree.append((word, postag))
            elif chunktag.startswith('B'):
                tree.append(Tree(chunktag[2:], [(word, postag)]))
            elif chunktag.startswith('I'):
                if (len(tree) == 0 or not isinstance(tree[-1], Tree) or
                            tree[-1].label() != chunktag[2:]):
                    if strict:
                        raise ValueError("Bad tag sequence")
                    else:
                        # Treat as B-*
                        tree.append(Tree(chunktag[2:], [(word, postag)]))
                else:
                    tree[-1].append((word, postag))
            elif chunktag == 'O':
                tree.append((word, postag))
            else:
                raise ValueError("Bad tag %r" % chunktag)
        return tree