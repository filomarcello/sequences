import unittest

from exceptions import SequenceException
from nucleic_acids import PureDNAseq, PureRNAseq, PureProteinSeq

seq1 = 'atcgatcggctacgattcga'
seq2 = 'acgcgaucgcgcgaucgauu'
seq3 = 'GPAVLIMCFYWHKRQNEDSTGPAVLIMCFYWH'

class TestSequence(unittest.TestCase):

    def setUp(self):
        self.DNA1 = PureDNAseq(seq1)
        self.RNA1 = PureRNAseq(seq2)
        self.prot1 = PureProteinSeq(seq3)

    def test_constructors(self):

        self.assertEqual(self.DNA1.seq, seq1)
        self.assertRaises(SequenceException, PureDNAseq, seq=seq2)

        self.assertEqual(self.RNA1.seq, seq2)
        self.assertRaises(SequenceException, PureRNAseq, seq=seq1)

        self.assertEqual(self.prot1.seq, seq3)
        self.assertRaises(SequenceException, PureProteinSeq, seq=seq1)


if __name__ == '__main__':
    unittest.main()
