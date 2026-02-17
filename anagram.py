# scrabble words for the following link: https://github.com/raun/Scrabble/blob/master/words.txt
WORD_LIST_PATH = 'words_scrabble.txt'
MAX_ANAGRAM_LENGTH = 6

def get_original_letters(max_anagram_length=int):
  """Takes in and validates user input to get the original letters for the anagrams.

  Args:
    max_anagram_length (int): The maximum length of the anagrams.

  Returns:
    str: The original letters for the anagrams.
  """
  while True:
    raw_input = input(f"Enter up to {max_anagram_length} letters: ").lower()
    original_letters = raw_input.replace(" ", "")

    if not original_letters.isalpha():
      print("Invalid input: Only letters are allowed (no numbers or special characters).")
    elif len(original_letters) > max_anagram_length:
      print(f"Invalid input: You must enter {max_anagram_length} or less letters.")
    else:
      return original_letters

def get_final_word_list(path=str, max_anagram_length=int):
  """Gets the final list of words that are within the max_anagram_length.

  Args:
    path (str): The path to the word list.
    max_anagram_length (int): The maximum length of the anagrams.

  Returns:
    list: The final list of words that are within the max_anagram_length.
  """
  words = []
  try:
    with open(path, 'r') as file:
      for line in file:
        word = line.strip()
        if 0 < len(word) <= max_anagram_length:
          words.append(word)
    return words
  except FileNotFoundError:
    print(f"Error: The file {path} was not found.")

def get_original_letters_dict(original_letters=str):
  """Gets the dictionary of the original letters.

  Args:
    original_letters (str): The original letters for the anagrams.

  Returns:
    dict: The dictionary of the original letters.
  """
  letters_dict = {}
  for letter in original_letters:
    letters_dict[letter] = letters_dict.get(letter, 0) + 1
  return letters_dict

original_letters = get_original_letters(MAX_ANAGRAM_LENGTH)
words = get_final_word_list(WORD_LIST_PATH, MAX_ANAGRAM_LENGTH)
letters_dict = get_original_letters_dict(original_letters)

final_list = []

for word in words:
  word = word.lower()
  copy_letters_dict = letters_dict.copy()
  
  is_anagram = True

  for letter in word:
    if copy_letters_dict.get(letter, 0) > 0:
      copy_letters_dict[letter] -= 1
    else:
      is_anagram = False
  
  if is_anagram:
    final_list.append(word)

print(final_list)