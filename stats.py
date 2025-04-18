def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    processed_text = list(text.lower())
    characters = {}
    for char in processed_text:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

#reference key for sorted dictionary
def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    char_list = []
    for char, count in dict.items():
        #removes none alphabet chars and puts them into seperate dicts in a list
        if char.isalpha():
            char_info = {"character": char, "count": count}
            char_list.append(char_info)
    return char_list

