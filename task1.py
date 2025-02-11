def get_dictionary(text):
    uniq_chars = set(list(text))
    dictionary = {c : 0 for c in uniq_chars}
    for char in text:
        dictionary[char] += 1
    return dictionary

try:
    with open('text.txt', 'r') as file:
        file_text = file.read()
        dict_frequency = get_dictionary(file_text)
        code = dict_frequency.values()
        print(dict_frequency)
        print(*code)
except FileNotFoundError as e:
    print(e)
