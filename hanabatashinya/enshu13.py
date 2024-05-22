def bubble_sort(num_list):

    for i in range(len(num_list)-1):
        for j in range(len(num_list)-(i+1)):
            if num_list[j+1] < num_list[j]:
                temp = num_list[j+1]
                num_list[j+1] = num_list[j]
                num_list[j] = temp

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
print(bubble_sort(num_list))


