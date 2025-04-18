from stats import get_num_words, get_num_characters, sort_on, sort_dict
import sys

def main():
    #Current book path
    #book_path = "./books/frankenstein.txt"
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    #converts the book to a string 
    text = get_book_text(book_path)

    #gets the number of words from the book
    num_words = get_num_words(text)
    print(f'Found {num_words} total words')
    
    #finds the number of characters in the book and puts them into a dictionary
    num_characters = get_num_characters(text)
    #puts the dictionary into a list and sorts by total number
    listed_char = sort_dict(num_characters)   
    listed_char.sort(reverse=True, key=sort_on)
 
    #prints the sorted dictionary in order
    for char_dict in listed_char:
        char = char_dict["character"]
        count = char_dict["count"]
        print(f'{char}: {count}') 

#opens the book filepath
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
