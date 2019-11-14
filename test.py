while True:
    data = input("Did your meal have any meat? Enter yes or no:")
    if data == "no":
        data = -4
    else:
        data = 4
    print(data)
    break

while True:
    data = input("Pick an answer from A to D:")
    if data.lower() not in ('a', 'b', 'c', 'd'):
        print("Not an appropriate choice.")
    else:
        break