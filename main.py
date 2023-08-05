def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_words(text)
    dict = get_dictionary(text)
    sorted_dict = sort_letters(dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    for item in sorted_dict:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    words = text.split()
    num = len(words)
    return num

def get_dictionary(text):
    dict = {}
    formatted = text.lower()
    for i in formatted:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

def sort_on(d):
    return d["num"]

def sort_letters(dict):
    sorted_list = []
    for i in dict:
        sorted_list.append({"char": i, "num": dict[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()