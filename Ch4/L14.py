def main_func(document: str, longest_word: str="") -> str:
    if document == "" or document.isspace():
        return longest_word
    
    words = document.split(maxsplit=1)
    if len(words[0]) > len(longest_word):
        longest_word = words[0]

    if len(words) > 1:
        return main_func(words[1], longest_word)
    else: 
        return longest_word
    

run_cases = [
    ("Either that wallpaper goes, or I do.", "wallpaper"),
    (
        "Then I die happy",
        "happy",
    ),
    (
        "Et tu, Brute?",
        "Brute?",
    ),
]

submit_cases = run_cases + [
    (
        "",
        "",
    ),
    (
        " ",
        "",
    ),
    (
        "Let us cross over the river and rest under the shade of the trees",
        "cross",
    ),
]

'''
Complete the find_longest_word function without a loop. It accepts string inputs, document, 
and optional longest_word, which is the current longest word and defaults to an empty string.

1. If document is empty or contains no words, then return longest_word. This is the base case.
2. Split the string into the first word and the rest of the string

|You can use .split with maxsplit=1 to split a string into a list of [first_word, rest_of_string]|

3. Check if the first word is longer than longest_word and update it if necessary
4. If the rest of the string exists, return the result of a recursive call on it
5. If no text remains, return the longest_word

Assume that a "word" means a series of any consecutive non-whitespace characters. For example, 
find_longest_word("How are you?") should return the string "you?".
'''