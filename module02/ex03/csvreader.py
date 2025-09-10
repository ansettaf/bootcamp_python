class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        self.data = None
        self._header = None

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r', encoding='utf-8')
        except Exception:
            return None
        lines = [line.rstrip('\n') for line in self.file.readlines()]
        if not lines:
            self.file.close()
            return None
        # split and check consistency
        parsed = [line.split(self.sep) for line in lines]
        lengths = [len(row) for row in parsed]
        if len(set(lengths)) != 1:
            self.file.close()
            return None
        if self.header:
            self._header = parsed[0]
            self.data = parsed[1 + self.skip_top: len(parsed) - self.skip_bottom]
        else:
            self.data = parsed[self.skip_top: len(parsed) - self.skip_bottom]
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.file:
                self.file.close()
        except Exception:
            pass
        return False

    def getdata(self):
        return [row[:] for row in self.data] if self.data is not None else None

    def getheader(self):
        return list(self._header) if self.header and self._header is not None else None
