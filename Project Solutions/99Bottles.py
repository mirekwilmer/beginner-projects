count = [i for i in range(1, 100)]
count = count[::-1]

for num in count:
    if num != 1:
        print("%s bottles of beer on the wall, %s bottles of beer.") % (num, num)
        print("Take one down and pass it around"),
        print("%s bottles of beer on the wall!\n") % (num - 1)
    if num == 1:
        print("%s bottle of beer on the wall, %s bottle of beer.") % (num, num)
        print("Take one down and pass it around"),
        print("No more bottles of beer on the wall!\n")

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall!\n")
