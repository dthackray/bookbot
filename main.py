def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    words = count_words(text)
    print(f"{words} found in the text.")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

main()