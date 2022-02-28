class File:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        print(sum(1 for row in self.file_obj))
        self.file_obj.seek(0)

        return self.file_obj

    def __exit__(self, file_type, value, exc_tb):
        self.file_obj.close()


with File('test.txt', 'r') as opened_file:
    pass
