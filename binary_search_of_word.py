def binary_word_search(filename, search_word):
    """
    Searches given search word in the file and returns True if found.
    :param filename: filename where text is stored to be searched.
    :param search_word: word to be searched entered by the user.
    :return: True if word is found else False.
    """
    my_list = []
    # Splitting the words and adding it to an empty list
    with open(filename, 'r') as f:
        for word in f:
            my_list.extend(word.lower().split())

    new_list = my_list
    # Traversing through the list to find the input word
    for i in range(len(new_list)):
        if search_word == new_list[i]:
            return True
        else:
            return False


if __name__ == "__main__":
    try:
        filename = "textfile.txt"
        # Taking input from the user
        word = input("Enter a word to be searched: ")
        print("Word is found.") if binary_word_search(filename, word) else print("Word is not found.")
    except FileNotFoundError:
        print("given file is not found...")
