import os.path
from solution import File
import tempfile

if __name__ == "__main__":
    path_to_file = 'some_filename'
    # print(os.path.exists(path_to_file))

    # file_obj = File(path_to_file)
    # print(os.path.exists(path_to_file))

    # print(file_obj.read())
    # print(file_obj.write('some text'))
    # print(file_obj.read())
    # print(file_obj.write('other text'))
    # print(file_obj.read())

    file_obj1 = File(path_to_file + '_1')
    file_obj2 = File(path_to_file + '_2')
    print(file_obj1.write('line 1\n'))
    print(file_obj2.write('line 2\n'))

    new_file_obj = file_obj1 + file_obj2
    print(isinstance(new_file_obj, File))
    print(new_file_obj)

    for line in new_file_obj:
        print(ascii(line))
    # print(os.path.join('some filename_1'))
    # f = tempfile.NamedTemporaryFile(delete=False)
    # print(f.name)
    # f.close()
    # print(tempfile.TemporaryFile().name)
    # print(path_to_file)
