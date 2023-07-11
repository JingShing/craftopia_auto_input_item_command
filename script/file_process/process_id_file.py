
def write_list_to_file(file_path, my_list):
    with open(file_path, 'w', encoding="utf-8") as file:
        for item in my_list:
            file.write(str(item) + '\n')

def read_file(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        lines = file.readlines()
    # print(lines)
    return lines

def remove_common_elements(list1, list2):
    unique_list1 = list(set(list1) - set(list2))
    unique_list2 = list(set(list2) - set(list1))
    print(unique_list1)
    print(unique_list2)
    return unique_list1, unique_list2

def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements

def process_id(list)->list:
    list_2 = process_id_to_list(list)
    # print(list_2)
    max_num = int(list_2[-1])
    list_num = []
    for i in range(1, max_num+1):
        list_num.append(i)
    final_list = remove_common_elements(list_num, list_2)[0]
    return final_list

def process_id_to_list(list)->list:
    list_2 = []
    for line in list:
        line.replace('\n', '')
        line = line.split(" ")[0]
        list_2.append(int(line))
    return list_2

def process_no_item_id():
    load_file_path = 'item_id.txt'
    save_file_path = 'only_id.txt'
    # write_list_to_file(save_file_path, read_file(load_file_path))
    write_list_to_file("process_id.txt", process_id(read_file(load_file_path)))

def id_item_key(list) -> dict:
    dict_2 = dict()
    for line in list:
        line = line.replace('\n', '')
        id = line.split(" ")[0]
        item = line.split(id+' ')[-1]
        dict_2[id] = item
    return dict_2

def dict_id_to_list(list, dict)->list:
    list_2 = []
    for i in list:
        line = str(i) + ' ' + dict[str(i)]
        list_2.append(line)
    return list_2

def process_old_item_id_leave_same():
    load_old_id_path = 'id_set/old_item_id.txt'
    list1 = process_id_to_list(read_file('id_set/process_id.txt'))
    list2 = process_id_to_list(read_file(load_old_id_path))
    list3 = find_common_elements(list1, list2)
    print(list3)
    dict_1 = id_item_key(read_file(load_old_id_path))
    list4 = dict_id_to_list(list3, dict_1)
    print(list4)
    write_list_to_file('id_set/old_items.txt', list4)

if __name__ == "__main__":
    process_old_item_id_leave_same()
