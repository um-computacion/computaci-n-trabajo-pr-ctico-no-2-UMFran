def is_palindrome(word):
    word = word.lower().replace(" ", "").replace(".", "").replace(",", "").replace(";", "").replace(":", "").replace("?", "").replace("!", "")