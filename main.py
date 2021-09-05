

def text_dict (file_name):
    with open(file_name, encoding="UTF-8") as file:
        # dict = {}
        index = 0
        list_string = []
        tuple1 = tuple()
        for line in file:
            index += 1
            # str_number = 'Строка номер ' + str(index) + ' файла номер ' + str(file_name)
            list_string.append(line.strip())
            length = len(list_string)
            # dict[str_number] = list_string
        tuple1 = (length, file_name, list_string)
    return tuple1

def list_dict (files):
    files_list = []
    for file in files:
        files_list.append(text_dict (file))
    files_list.sort(key=lambda x: x[0])
    return files_list
files_list = list_dict (['1.txt', '2.txt', '3.txt'])


def Write_file(files_list, file_name):
    with open(file_name, 'w', encoding="UTF-8") as f:
        for file in files_list:
            f.write(file[1] + '\n')
            f.write(str(file[0])+ '\n')
            for string in file[2]:
                f.write(string + '\n')
    return






Write_file(files_list, '4.txt')
