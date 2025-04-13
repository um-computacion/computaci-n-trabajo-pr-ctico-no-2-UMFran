def is_palindrome(word):
    word = word.lower().replace(" ", "").replace(".", "").replace(",", "").replace(";", "").replace(":", "").replace("?", "").replace("!", "")

    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])