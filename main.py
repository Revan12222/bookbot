from stats import get_word_count
from stats import get_book_text
from stats import get_char_count
from stats import nice_printout
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    input_file = sys.argv[1]
    contents = get_book_text(input_file)
    num_words = get_word_count(contents)
    #print(f"{num_words} words found in the document")
    characters = get_char_count(contents)
    nice_printout(num_words,characters)


main()
