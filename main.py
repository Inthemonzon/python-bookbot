from stats import get_num_words, get_num_char, sort_on, chars_dict_to_sorted_list
import sys

def get_book_text(path):
	with open(path) as f:
		return f.read()

def main():
	if len(sys.argv) != 2: 
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	path_to_file = sys.argv[1]
	text = get_book_text(path_to_file)
	num_words = get_num_words(text)
	num_char = get_num_char(text)
	sorted_chars = chars_dict_to_sorted_list(num_char)
	print_report(path_to_file, num_words, sorted_chars)

def print_report(path_to_file, num_words, sorted_chars):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path_to_file}...") 
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in sorted_chars: 
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")

main()

