def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print("\n--- Begin report of books/frankenstein.txt ---\n")
    words = count_words(text)
    print(f"{words} words found in the text.\n")
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
    characters_dict = sorted(characters_dict.items(), key=lambda x: x[1], reverse=True)

    characters_list = list(characters_dict)
    for character in characters_list:
        if character[0].isalpha():
            print(f"The '{character[0]}' character was found {character[1]} times.")

main()