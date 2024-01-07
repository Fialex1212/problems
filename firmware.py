'''

Write a function to taka a list of strings each containing a firmware
version number and return the greatest firmware version. An example of a
firmware version string would be "cam-1.6.12400" of "cam-1.17.11500".

'''

import random


def generate_firmware(amount: int) -> list:
    firmwares = [f"cam-{random.randint(1, 20)}.{random.randint(1, 60)}.{round(random.randint(10000, 20000), -2)}"for i in range(amount)]
    nums = []
    format_nums = []
    for i in firmwares:
        num = i.index('-')
        num = i[num:]
        nums.append(str(num))
    for i in nums:
        i = i.split('.')
        i = [abs(int(j)) for j in i]
        format_nums.append(i)
    print(firmwares)
    return format_nums


def findout_max(lst: list) -> str:
    max_firmware = list(max(lst))
    output = "The greatest firmware is: cam-"
    for i in max_firmware:
        output += str(i)+"."
    return print(output)

lst = generate_firmware(10)
findout_max(lst)