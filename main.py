def main():
    book_path = "github.com/justfancy64/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = sort(chars_dict)
    for i in sorted_chars:
        print(f"The {i} character was found {sorted_chars[i]} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort(chars_dict):
     order = {}
     sorted_list = sorted(chars_dict.items(), key=lambda x:x[1],reverse=True)
     for i in sorted_list:
         order[i[0]] = i[1]
     return order

main()