import os.path
import tempfile
import uuid


class File:

    def __init__(self, filepath):
        self.counter = 0
        self.path = filepath
        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                f.write('')

    def read(self):
        with open(self.path, 'r') as f:
            result = f.read()
            if result is None:
                return ''
        return result

    def write(self, data):
        with open(self.path, 'w') as f:
            size = f.write(data)
        return (size if (type(size) == int and size > 0) else 0)

    def __add__(self, obj):
        unique_filename = str(uuid.uuid4().hex)
        path = os.path.join(tempfile.gettempdir(), unique_filename)
        new_file = File(path)
        new_file.write(self.read() + obj.read())
        return new_file

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.counter)
            line = f.readline()

            if not line:
                self.counter = 0
                raise StopIteration('EOF')

            self.counter = f.tell()
        return line

    def __str__(self):
        return self.path
