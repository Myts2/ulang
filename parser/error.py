# decompyle3 version 3.3.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.5 (default, Oct 18 2019, 16:29:31) 
# [GCC 5.4.0 20160609]
# Embedded file name: ulang\parser\error.py


class SyntaxError(ValueError):

    def __init__(self, message, filename, lineno, colno, source=None):
        self.message_ = message
        self.filename_ = filename
        self.lineno_ = lineno if lineno > 0 else 1
        self.colno_ = colno if colno > 0 else 1
        self.source_ = source

    def __str__(self):
        msg = 'File "%s", line %d:%d, %s' % (
         self.filename_, self.lineno_, self.colno_, self.message_)
        if self.source_:
            line = self.source_[(self.lineno_ - 1)]
            col = ' ' * (self.colno_ - 1) + '^'
            msg = '%s\n%s\n%s' % (msg, line, col)
        return msg