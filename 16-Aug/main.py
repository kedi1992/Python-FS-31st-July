# data = [10, 20, 30]
#
# data.append(40)
# data.append(50)
# data.append(60)
# print("after append :: ", data)
# print("first element is : ", data[0])
# print("last ele is      : ", data[-1])
#
# deleted_ele = data.pop()
# print(f"deleted element is : {deleted_ele}")
# print(f"list after pop : {data}")
#
# remove_ele = 10
# print(f"before removing {remove_ele} element : {data}")
# data.remove(remove_ele)
# print(f"after removing {remove_ele} element : {data}")
#
# check_count = 10
# print(f"count of {check_count} is : {data.count(check_count)}")
#
# index_element = 20
# print(f"index of element {index_element} is {data.index(index_element)}")
#
# print(f"list before sort :: {data}")
# data.sort(reverse=True)
# print(f"list after sort :: {data}")
#
# print("before insert :: ", data)
# data.insert(2, 200)
# print("after insert : ", data)
#
# print(f"before reverse : {data}")
# data.reverse()
# print("after reverse :: ", data)
#
#
# print("before extend :: ", data)
# data.extend([101, 202, 303])
# print("after extend :: ", data)
#
# data2 = data.copy()
# data2[0] = 999
# print("data  :: ", data)
# print("data2 :: ", data2)
#
# data.clear()
# print(f"list after clean : {data}")
# print(f"list before pop : {data}")




data = [1,2,3,4, [5,6,7, [8, [100, 200, 300, [588, 88]]]]]
# 1,2,3,4,5,6,7,8

# for num in data:
#     print(num)

main_data = []

def get_element(data):
    for e in data:
        if type(e) == list:
            get_element(e)
        else:
            main_data.append(e)

get_element(data)

print(main_data)