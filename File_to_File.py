import os.path
import tempfile
import uuid


class File:
    def __init__(self, path):
        self.path = path

        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def __add__(self, other):
        new_file_path = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
        new_file = type(self)(new_file_path)
        new_file.write(self.read() + other.read())
        return new_file

    def __iter__(self):
        self.curr = 0
        with open(self.path, "r") as f:
            self.lines = f.readlines()
        return self

    def __next__(self):
        try:
            line = self.lines[self.curr]
            self.curr += 1
            return line
        except IndexError:
            raise StopIteration

    def __str__(self):
        return self.path

    def read(self):
        with open(self.path, "r") as f:
            return f.read()

    def write(self, data):
        with open(self.path, "w") as f:
            f.write(data)

path_to_file = 'file_6.txt'
print(os.path.exists(path_to_file))
file_obj = File(path_to_file)
print(os.path.exists(path_to_file))
print(file_obj)
file_obj.write('some text')
print(file_obj.read())
file_obj.write('another text')
print(file_obj.read())
file_obj_1 = File(path_to_file + '_1')
print(file_obj_1)
file_obj_1.write('line 1\n')
file_obj_2 = File(path_to_file + '_2')
print(file_obj_2)
file_obj_2.write('line 2\n')
print(file_obj_1.read())
print(file_obj_2.read())
new_file_obj = file_obj_1 + file_obj_2
print(isinstance(new_file_obj, File))
print(new_file_obj)
for line in new_file_obj:
    print(ascii(line))
new_path_to_file = str(new_file_obj)
print(os.path.exists(new_path_to_file))
file_obj_3 = File(new_path_to_file)
print(file_obj_3)
