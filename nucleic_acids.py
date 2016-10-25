""" created 25/10/2016
author: marcello
version: 0.1
"""
from exceptions import SequenceException

# constants

SEQ_CHARS = {'DNA': set('atcg'),
             'RNA': set('aucg'),
             'protein': set('GPAVLIMCFYWHKRQNEDST')}
# classes

class Sequence():
    """Base class for sequences."""

    def __init__(self, seq: str, type: str):
        """type may be 'DNA', 'RNA', 'protein'. """
        s = set(seq)
        if not s <= SEQ_CHARS[type]:
            exp = ''
            mes = 'Character(s) not admitted in DNA sequence'
            raise SequenceException(message=mes, expression=exp)
        else:
            self._seq = seq
            self._type = type

# properties

    @property
    def seq(self):
        return self._seq

    @property
    def type(self):
        return self._type

# methods

    def reverse(self):
        """Reverses the sequence, without complement"""
        pass

    def complement(self):
        """Makes the sequence complementary. Only nucleic acids."""
        pass

    def rev_compl(self):
        """Reverses and complements the sequence. Only nucleic acids."""
        pass

    def to_RNA(self):
        """Returns another RNA sequence."""
        pass

    def to_DNA(self):
        """Returns another DNA sequence."""
        pass

    def to_protein(self):
        """Returns another protein sequence."""
        pass


    def __str__(self):
        return self._seq


class PureDNAseq(Sequence):
    """DNA sequences containing only a, t, g, c characters."""

    def __init__(self, seq: str = '', type='DNA'):
        super().__init__(seq, type)


class PureRNAseq(Sequence):
    """DNA sequences containing only a, u, g, c characters."""

    def __init__(self, seq: str = '', type='RNA'):
        super().__init__(seq, type)


class PureProteinSeq(Sequence):
    """DNA sequences containing only a, u, g, c characters."""

    def __init__(self, seq: str = '', type='protein'):
        super().__init__(seq, type)