def get_book_text(book):
    with open(book) as f:
        return f.read()
    
def main():
    result = get_book_text("books/frankenstein.txt")
    print(result)

if __name__ == "__main__":
    main()
