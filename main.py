path_to_file = "books/frankenstein.txt"

def num_of_chars(book):
    char_counter = {}
    lowered_text= book.lower()

    for char in lowered_text:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1

    return char_counter
    

def num_of_words(book):
    words = book.split()
    return len(words)


def sort_on(dictionary):
    return dictionary["num"]


def sort_dictionary(dictionary):
    list_of_dictionary = []
    for key in dictionary:
        if key.isalpha():
            list_of_dictionary.append({"character": key, "num": dictionary[key]})

    list_of_dictionary.sort(reverse=True, key=sort_on)
    return list_of_dictionary


def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_of_words(file_contents)} words found in the document\n")

    char_counter = num_of_chars(file_contents)
    char_counter = sort_dictionary(char_counter)

    for char in char_counter:
        print(f"The '{char['character']}' character was found {char['num']} times")


main()
