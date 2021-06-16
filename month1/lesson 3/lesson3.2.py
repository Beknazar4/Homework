name = input()
age = int(input())
hobby = input()

if name == "Ali" and age > 17 and hobby == "1% of tiktok":
    print("Ты Али")
else:
    print("Ты не Али, ты школьник")

if name == "Ali" or age > 17 or hobby == "1% of tiktok":
    print("Ты либо Али, либо старше 17, либо твое хобби Тикток")
else:
    print("Ты вообще не подходишь под эти условия!")
