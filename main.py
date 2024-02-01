def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    words = count_words(text)
    print(f"{words} words found in the text.")
    characters = count_characters(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    number_of_words = len(words)
    return number_of_words

def count_characters(text):
    characters_dict = {e:text.count(e) for e in sorted(set(text.lower()))}
    return characters_dict

main()