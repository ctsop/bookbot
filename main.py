def get_book_text(book):
    with open(book) as f:
        return f.read()
    
def count_words(result):
    return len(result.split())
    
def main():
    result = get_book_text("books/frankenstein.txt")
    num_words = count_words(result)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()
