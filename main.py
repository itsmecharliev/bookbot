from stats import get_num_words, get_num_chars, sorted_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    contents = get_book_text(sys.argv[1])
    num_words = get_num_words(contents)
    num_chars = sorted_dictionary(get_num_chars(contents))
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in num_chars:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num_times"]}")
    print("============= END ===============")


main()
