import os
from tempfile import mkstemp

class MarkdownProcessor(object):

    def on_source_read(self, app, docname, source):
        if docname == 'index':
            return

        try:
            input = mkstemp()
            output = mkstemp()
            os.close(input[0])
            os.close(output[0])

            with open(input[1], 'bw') as f:
                f.write(source[0].encode('utf-8'))

            cmdline = "pandoc -f markdown_github+definition_lists -t rst  %s -o %s" % (input[1], output[1])
            os.system(cmdline)

            source[0] = open(output[1], 'br').read().decode('utf-8')

        finally:
            os.unlink(input[1])
            os.unlink(output[1])

    def setup(self, app):
        app.connect('source-read', self.on_source_read)


def setup(app):
    md = MarkdownProcessor()
    md.setup(app)
