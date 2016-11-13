import unittest

import data.analysis.train as train


class ChunkTaggerTest(unittest.TestCase):

    def test_computer_science_tagger(self):
        self.assertTrue(train.train_computer_science(False))

if __name__ == "__main__":
    unittest.main()
