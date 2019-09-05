
class MafftFragment:
    def __init__(self, name, seq):
        self.id = name
        self.seq = seq

    def __str__(self):
        return u'Id: %s Sequence: %s' % (str(self.id), str(self.seq))

    def __len__(self):
        return len(self.seq)

    def __getitem__(self, index):
        return self.seq[index]
