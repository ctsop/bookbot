from stats import count_words, count_character, sort_dictionary
import sys

def get_book_text(book):
    with open(book) as f:
        return f.read()
     
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_location = sys.argv[1]
    result = get_book_text(file_location)
    num_words = count_words(result)
    num_char = count_character(result)
    sorted_list = sort_dictionary(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_location}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for sort in sorted_list:
        if sort["char"].isalpha():
            print(f"{sort["char"]}: {sort["num"]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
