import string

def is_sentence_palindrome(sentence):
    # Remove punctuation and spaces, convert to lowercase
    cleaned = ''.join(
        ch.lower() for ch in sentence if ch.isalnum()
    )
    return cleaned == cleaned[::-1]
#test cases1:
#"A man, a plan, a canal, Panama" #is a palindrome
#test cases2:
# Was it a car or a cat I saw? #is not a palindrome
sentence = input("Enter a sentence: ")
if is_sentence_palindrome(sentence):
    print("The sentence is a palindrome.")
else:
    print("The sentence is not a palindrome.")