def count_words(sentence):
    words=sentence.split()
    return len(words)

text=input("please enter the text:")
print("the number of words in the given text:",count_words(text))

