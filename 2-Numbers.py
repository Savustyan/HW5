import sys
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
]

for number in numbers:
    if number == 237:
        sys.exit(0)
    if number %2 == 0:
        print(number)