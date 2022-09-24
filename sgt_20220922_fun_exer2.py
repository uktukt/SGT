# 2. Palindrome
# Write the function is_palindrome(text)
# which returns a bool True or False depending on whether the word or sentence is read equally from both sides.
# PS You can start with a one-word solution from the beginning, but the full solution will ignore whitespace and uppercase and lowercase letters.


# is_palindrome ("Alus ari i ra    sula") -> True
# is_palindrome("ABa") -> True
# is_palindrome("nava") -> False

def is_palindrome(some_text):
    format_text = some_text.lower().replace(" ","")
    if format_text==format_text[::-1]:
        result=True
    else:
        result=False
    return result

my_text  = input("Input text: ")
print(is_palindrome(my_text))