import nltk
import engine
import filters

summary = engine.filter_summary(filters.test_summary)

sentences = nltk.sent_tokenize(summary)

sentences = [nltk.word_tokenize(sent) for sent in sentences]

sentences = [nltk.pos_tag(sent) for sent in sentences]

grammar = "NP: {<DT>?<JJ>*<NN>}"

chunkParser = nltk.RegexpParser(grammar)

for sentence in sentences:
	result = chunkParser.parse(sentence)
	result.draw()