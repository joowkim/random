import gzip


class ParseFastQ(object):
    """Returns a read-by-read fastQ parser analogous to file.readline()"""

    def __init__(self, filePath):
        """Returns a read-by-read fastQ parser analogous to file.readline().
        Exmpl: parser.next()
        -OR-
        Its an iterator so you can do:
        for rec in parser:
            ... do something with rec ...
        rec is tuple: (seqHeader,seqStr,qualHeader,qualStr)
        """
        if filePath.endswith('.gz'):
            self._file = gzip.open(filePath)
        else:
            self._file = open(filePath, 'rU')

        tmp = self._file.readline()
        header = tmp.split()[0].rsplit(":", 2)[0]

        self._file.seek(0)
        self._currentLineNumber = 0
        self._hdsym = header

    def __iter__(self):
        return self

    def __next__(self):
        """Reads in next element, parses, and does minimal verification.
        Returns: tuple: (seqHeader,seqStr,qualHeader,qualStr)"""
        # ++++ Get Next Four Lines ++++
        ele_list = []
        if self._file.readline().startswith(self._hdsym):
            ele_list.append(self._file.readline().rstrip())





        for i in range(4):
            line = self._file.readline()
            self._currentLineNumber += 1  ## increment file position
            if line:
                ele_list.append(line.strip('\n'))
            else:
                ele_list.append(None)

        # ++++ Check Lines For Expected Form ++++
        trues = [bool(x) for x in ele_list].count(True)
        nones = ele_list.count(None)
        # -- Check for acceptable end of file --
        if nones == 4:
            raise StopIteration
        # -- Make sure we got 4 full lines of data --
        assert trues == 4, \
            "** ERROR: It looks like I encountered a premature EOF or empty line.\n\
            Please check FastQ file near line number %s (plus or minus ~4 lines) and try again**" % (
                self._currentLineNumber)
        # -- Make sure we are in the correct "register" --
        assert ele_list[0].startswith(self._hdsym[0]), \
            "** ERROR: The 1st line in fastq element does not start with '%s'.\n\
            Please check FastQ file near line number %s (plus or minus ~4 lines) and try again**" % (
                self._hdsym[0], self._currentLineNumber)
        assert ele_list[2].startswith(self._hdsym[1]), \
            "** ERROR: The 3rd line in fastq element does not start with '%s'.\n\
            Please check FastQ file near line number %s (plus or minus ~4 lines) and try again**" % (
                self._hdsym[1], self._currentLineNumber)
        # -- Make sure the seq line and qual line have equal lengths --
        assert len(ele_list[1]) == len(ele_list[3]), "** ERROR: The length of Sequence data and Quality data of the last record aren't equal.\n\
               Please check FastQ file near line number %s (plus or minus ~4 lines) and try again**" % (
            self._currentLineNumber)

        # ++++ Return fatsQ data as tuple ++++
        return tuple(ele_list)
