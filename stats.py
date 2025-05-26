def count_words(result):
    return len(result.split())

def count_character(result):
    character_dict = {}

    for res in result:
        if res.lower() in character_dict:
            character_dict[res.lower()] += 1
        else:
            character_dict[res.lower()] = 1
    return character_dict

def sort_on(character_dict):
    return character_dict["num"]

def sort_dictionary(character_dict):
    character_list = []
    for char in character_dict:
        character_list.append({"char": char, "num": character_dict[char]})
    character_list.sort(reverse=True, key=sort_on)
    return character_list

