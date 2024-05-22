kurai_list = ["億", "万", ""]
tani_list = ["千", "百", "十", ""]
kazu = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
num_list = [[0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
keta = 0

arabia = int(input())

if arabia == 0 or arabia == 1:
    print(kazu[arabia])
    exit()

while arabia != 0:
    num_list[-(keta // 4 + 1)][-(keta % 4 + 1)] = arabia % 10
    arabia //= 10
    keta += 1

for row in range(len(num_list)):
    for index in range(len(num_list[row])):
        flag = 0
        if num_list[row][index]:
            flag = 1
            print(f"{kazu[num_list[row][index]]}{tani_list[index]}", end="")
    if flag:
        print(kurai_list[row], end="")