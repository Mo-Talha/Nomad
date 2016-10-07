import nltk


class ChunkTagger(nltk.TaggerI):
    def __init__(self, train_sentences):
        train_set = []
        for tagged_sent in train_sentences:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                feature_set = self.chunk_features(tagged_sent, i, history)
                train_set.append((feature_set, tag))
                history.append(tag)
                #algorithm='megam'
        self.classifier = nltk.MaxentClassifier.train(train_set, trace=0)

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
        return {"pos": pos}