def simple_sort(num_list):
    if len(num_list) == 0:
        print("pls number list")
        exit(0)
    else:
        min_index = 0

    for i in range(len(num_list)-1):
        min_index = i
        for j in range(i+1, len(num_list)):
            if num_list[j] < num_list[min_index]:
                print(str(num_list[j]) + " < " + str(num_list[min_index]))
                min_index = j

        if i != min_index:
            print(str(num_list[i]) + " change " + str(num_list[min_index]))
            temp = num_list[i]
            num_list[i] = num_list[min_index]
            num_list[min_index] = temp

    return num_list


input_str = ""
num_list = []


while input_str != "sort":
    try:
        input_str = input("数字を入力 or sortでソート")
        input_num = int(input_str)
        num_list.append(input_num)
    except ValueError:
        print(input_str, input_num)
        if input_str == "sort":
            break
        else:
            print("数字を入力して")

print(num_list)
print(simple_sort(num_list))


