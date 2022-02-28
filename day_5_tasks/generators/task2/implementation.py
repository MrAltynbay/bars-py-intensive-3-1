from contextlib import contextmanager


@contextmanager
def open_file(name):
    file = open(name, 'r')
    msg = 'ERROR'
    print([row.rstrip() for row in file if msg in row])
    file.seek(0)
    yield file
    file.close()


with open_file('log.txt') as f:
    pass
