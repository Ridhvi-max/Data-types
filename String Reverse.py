class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        return ' '.join(self.text.split()[::-1])
sentence = "Hello I am Ridhvi Shringi"
reverser = StringReverser(sentence)
print(reverser.reverse_words())