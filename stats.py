def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            if char.isprintable():
                chars[char] = 1

    return chars

def sort_on(dict):
    return dict["num_times"]

def sorted_dictionary(dict):
    new_dict = []
    for k in dict:
        new_dict.append({"char" : k, "num_times" : dict[k]})
    new_dict.sort(reverse=True, key=sort_on)
    return new_dict
