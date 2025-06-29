def get_book_text(filepath):
    file_contents = ''
    with open(filepath,'r') as f:
        file_contents = f.read()
    return file_contents

def get_word_count(book):
    words = book.split()
    return len(words)

def get_char_count(book):
    counter_dict = {}
    book = book.lower()
    for char in book:
        if char in counter_dict.keys():
            counter_dict[char]+=1
        elif char == " " or char == "\n":
            continue
        else:
            counter_dict[char]=1
    sorted_counter = {}
    for i in range(0,len(counter_dict)):
        max = -1
        max_key = None
        for key,value in counter_dict.items():
            if value > max:
                max = value
                max_key = key
        sorted_counter.update({max_key:max})
        del counter_dict[max_key]
    return sorted_counter

def nice_printout(word_count, character_dict):
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for key,value in character_dict.items():
        print(f"{key}: {value}")
    print("============= END ===============")
    return None
