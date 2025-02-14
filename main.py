def read_book(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    

def count_words(string):
    return len(string.split())


def count_characters(string):
    letter_histogram = {}
    for char in string.lower():
        if not char.isalpha():
            continue
        if char not in letter_histogram:
            letter_histogram[char] = 1
        else:
            letter_histogram[char] += 1

    return letter_histogram


def dict_to_list_of_dicts(dict):
    list = []
    for entry in dict:
        new_entry = {}
        new_entry["letter"] = entry
        new_entry["count"] = dict[entry]
        list.append(new_entry)
    return list


def sort_on(dict):
    return dict["count"]


def main():
    file_path = "books/frankenstein.txt"
    book = read_book(file_path)

    print(f"--- Begin report of {file_path} ---")
    print(f"Words in book: {count_words(book)}.")

    character_counts = count_characters(book)
    list_of_charaters = dict_to_list_of_dicts(character_counts)

    # Sort by descending occurence
    list_of_charaters.sort(reverse=True, key=sort_on)
    
    for l in list_of_charaters:
        print(f"The '{l["letter"]}' character was found {l["count"]} times")
    print("--- End report ---")
main()
