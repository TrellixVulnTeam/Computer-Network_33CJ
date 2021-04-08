def list_to_dict(arr):
    tmp = {}
    for value in arr:
        try:
            tmp[value.upper()] += 1
        except KeyError:
            tmp[value.upper()] = 1
    return tmp


data = ["A", "B", "C", "A", "a", "b"]

data3 = list_to_dict(data)

# data2 = {}
# while True:
#     tmp = input("Enter: ").upper()
#     if tmp == 'EXIT':
#         break
#     try:
#         data2[tmp] += 1
#     except KeyError:
#         data2[tmp] = 1

print(data3)
food = input("Name: ").upper()
while True:
    amount = abs(int(input("Amount: ")))
    if amount < data3[food]:
        data3[food] -= amount
        break
    elif data3[food] == amount:
        print("pass")
        data3.pop(food, None)
        break
    print("Please Correct")

print(data3)

