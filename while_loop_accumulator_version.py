def get_starting_number():
    while True:
        number = input("How many bottles of beer on the wall?")
        if number.isnumeric() == True and int(number)>=1:
            return int(number)

def sing(number):
    num = 0
    while num < number:
        num_befor = number - num
        num_after = num_befor - 1
        if num == number - 1:
            print(f"{num_befor} bottles of beer on the wall, {num_befor} bottles of beer.")
            print(f"Take one down, pass it around, no more bottles of beer on the wall!")
            return
        print(f"{num_befor} bottles of beer on the wall, {num_befor} bottles of beer.")
        print(f"Take one down, pass it around, {num_after} bottles of beer on the wall.\n")
        num += 1

