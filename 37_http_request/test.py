# def dec_to_roman(decimal):
#     dec_rom_dict = [
#         (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
#         (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
#         (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
#     ]
#
#     result = ''
#     for value, numeral in dec_rom_dict:
#         while decimal >= value:
#             result += numeral
#             decimal -= value
#
#     return result
#
# # Example usage:
# decimal_number = 1987
# roman_numeral = dec_to_roman(decimal_number)
# print(roman_numeral)

# arr = [0, 2, 5, 9, 7, 1, 6, 3, 8, 4]
# len_arr = len(arr)
#
# count = 0
# for i in range(len_arr):
#     j = i + 1
#     for j in range(i+1, len_arr):
#         if arr[i] > arr[j]:
#             count += 1
# print(count)

#
# arr = [0, 2, 5, 9, 7, 1, 6, 3, 8, 4]
#
# count = 0
# n = len(arr)
#
# for i in range(n):
#     for j in range(i + 1, n):
#         if arr[i] > arr[j]:
#             count += 1
#
# print("The number of inversions is:", count)
def inversion(array):
    count = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                count += 1
                print(f"{array[i]} > {array[j]}: inversion")
    print(f"Total count: {count}")


arr = [0, 2, 5, 9, 7, 1, 6, 3, 8, 4]
inversion(arr)