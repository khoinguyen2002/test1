input_list = [2, 4, 4, 8, 1,22, 64, 16]
output_list = []

for index, section in enumerate(input_list):
    sibling = 128 / section
    add = True
    for ind in range(index + 1, len(input_list)):
        if input_list[ind] == section:
            add = False
            break
    if add:
        for i in range(index + 1, len(input_list)):
            if input_list[i] == sibling:
                temp_dict = {
                        "first_num": section,
                        "first_index": index,
                        "second_num": int(sibling),
                        "second_index": i
                    }
                output_list.append(temp_dict)
                break

for answer in output_list:
    print("first: " + str(answer['first_num']) + ", index: " +
          str(answer['first_index']) + " - second: " + str(answer['second_num']) +
          ", index: " + str(answer['second_index'])
)