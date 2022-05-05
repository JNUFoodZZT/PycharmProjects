class Count():
    def __init__(self,filename):
        self.filename = filename

    def word_count(self):
        word = input('the word is:')
        with open(self.filename) as f_obj:
            contents = f_obj.read()
            counts = contents.lower().count(word)
        print(counts)

lover = Count('lover.txt')
lover.word_count()

