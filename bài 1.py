
number_input = input("Nhập dãy số, cách nhau bởi dấu ' ': ")

number_list = number_input.split(" ")

for i in range(len(number_list) - 1, -1, -1):
    print(number_list[i])

