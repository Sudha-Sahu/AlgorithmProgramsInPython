# program for searching the number in given array using binary search.


def binary_search_of_number(int_list, low, high, search):
    if low <= high:
        mid = (low + high) // 2
        if int_list[mid] == search:
            return mid
        elif int_list[mid] > search:
            return binary_search_of_number(int_list, low, mid - 1, search)
        else:
            return binary_search_of_number(int_list, mid + 1, high, search)
    else:
        return -1


int_array = [12, 56, 89, 89, 90, 95, 99]
find_num = int(input("enter any number from the list to search: "))

# Function call
output = binary_search_of_number(int_array, 0, len(int_array) - 1, find_num)

if output == -1:
    print("given number is not present in the given list ")
else:
    print("given number is present in the given list at index : ", output)
