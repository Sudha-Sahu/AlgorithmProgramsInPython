# program for searching the number in given array using binary search.

def binary_search_of_string(string_arr, find_str):
    start = 0
    end = len(string_arr)
    while start <= end:
        m = (start + end) // 2
        res = (find_str == string_arr[m])
        if res == 0:
            return m - 1
        elif res > 0:
            start = m + 1
        else:
            end = m - 1
    return "not available"


if __name__ == "__main__":

    fruits = ["apple", "banana", "orange", "papaya", "pear", "mango"]
    search_fruit = input("enter any fruit name to search from the fruit list: ")
    op = binary_search_of_string(fruits, search_fruit)

    if op == "not available":
        print("given fruit is not present in the fruit list ")
    else:
        print("given fruit is present in the fruit list at the index: ", op)
