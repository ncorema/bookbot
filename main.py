def main():
    book_path = "books/frankenstein.txt"
    book_content = get_text(book_path)

    word_count = wordcount(book_content)
    letter_dict = letter_count(book_content)
    letter_list = create_letter_list(letter_dict)

    bookreport(book_path, word_count, letter_list)
    
    
    
def wordcount(content):
    words = content.split()
    return len(words)

def get_text(path):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def letter_count(content):
    letter_dict = {}
    for letter in content:
        lowercase_letter = letter.lower()
        if lowercase_letter in letter_dict.keys():
            letter_dict[lowercase_letter] += 1
        else:
            letter_dict[lowercase_letter] = 1

    sorted_dict = dict(sorted(letter_dict.items()))
    return sorted_dict

def sort_on(dict):
    return dict["num"]

def create_letter_list(dictionary):
    list_of_letters = []
    letterdict = {}
    for letter in dictionary.keys():
        if letter.isalpha():
            letterdict = {
                "letter": letter,
                "num": dictionary[letter]
            }
            list_of_letters.append(letterdict)
    list_of_letters.sort(reverse=True, key=sort_on)
    return list_of_letters

def bookreport(book_path, wordcount, list_of_letters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{wordcount} words found in the document")
    print()

    for letter_dict in list_of_letters:
        l = letter_dict["letter"]
        n = letter_dict["num"]
        print(f"The {l} character was found {n} times")
    print("--- End report ---")




main()