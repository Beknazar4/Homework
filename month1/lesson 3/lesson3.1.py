age = int(input())

if age > 18:
    name = input()
    if name == "Beknazar":
        hobby = input()
        if hobby == "drawing":
            print("Вы не умеете рисовать")
        else:
            print("Вы умеете петь")
        print("Ваc зовут Бекназар")
    else:
        print("Вы не Бекназар")
else:
    print("Вам нельзя!")