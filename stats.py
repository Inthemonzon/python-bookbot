def get_num_words(text):
        words = text.split()
        return len(words)

def get_num_char(text):
	char_count = {}
	lower_text = text.lower()
	for char in lower_text:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count

def sort_on(item):
    return item["num"]
				
def chars_dict_to_sorted_list(char_count):
	sorted_list = []
	for char in char_count:
		sorted_list.append({"char": char, "num": char_count[char]})
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list
