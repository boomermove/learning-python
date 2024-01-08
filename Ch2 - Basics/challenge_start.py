# Python code​​​​​​‌​‌​‌​​‌‌‌​​​‌​‌​‌​‌‌​​​​ below
# Use print("messages...") to debug your solution.
import string

show_expected_result = False
show_hints = False

def is_palindrome(teststr):
    formatstr = teststr.replace(" ", "").translate(str.maketrans('', '', string.punctuation)).lower()
    revstr = formatstr [::-1]
    
    if revstr == formatstr:
      return True
  
    return False
  
# This is how your code will be called.
# Your function should return whether a string is a palindrome.
# The code will count the number of correct answers.
total = 0
test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.","Race car!"]
for word in test_words:
    # total += Answer.is_palindrome(word)
    total += is_palindrome(word)
    print(total)