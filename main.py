# Copied solution from bootdev exercise
# Task 1 - Read the book. Change main.py so that instead of printing "hello world", it reads the contents of the "frankenstein.txt" and 
#           prints it all to the console.
# Task 2 - Count words. Add a new function to your script that takes the text from the book as a string, and returns the number of words 
#           in the string....77986 words total
# Task 3 - Count Characters. Add a new function to your script that takes the text from the book as a string, and returns the number of times
#           each character appears in the string. Convert any character to lowercase, we don't want duplicates.
# Task 4 - Print a Report. Let's aggregate all the word and character data into a nice report that we can print to the console!

# Task 1: print book text...print line commented out
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # Task1: print lines of text
    # print(text) # previous step to output to command line

    # Task2: num words printed to screen
    num_words = get_num_words(text)
    # print(f"{num_words} words found in the document")
    
    # Task3: count characters and print to the screen
    chars_dict = get_chars_dict(text)
    
    # Task #4 - count number characters per line
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
    
###  Rmvove for Task #4 
#    from Task #3 - print to screen   
#    print(chars_dict)
#    
#   Task 2: num words in a file
#   def get_num_words(text):
#       words = text.split()
#       return len(words)
#########

# Task3: Count characters
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# Task 1 : get book text
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Just runs the main function definition
main()
