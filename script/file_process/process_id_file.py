
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

def process_id(list):
    list_2 = []
    for line in list:
        line.replace('\n', '')
        line = line.split(" ")[0]
        list_2.append(int(line))
    # print(list_2)
    max_num = int(list_2[-1])
    list_num = []
    for i in range(1, max_num+1):
        list_num.append(i)
    final_list = remove_common_elements(list_num, list_2)[0]
    return final_list

if __name__ == "__main__":
    load_file_path = 'item_id.txt'
    save_file_path = 'only_id.txt'
    # write_list_to_file(save_file_path, read_file(load_file_path))
    write_list_to_file("process_id.txt", process_id(read_file(load_file_path)))
