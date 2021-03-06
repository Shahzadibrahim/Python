
# # Daily Chalange

class Text():

    def __init__(self,text):
        self.text = text
        self.most_used = None

    @staticmethod
    def from_file(file_path):
        with open('thestranger.txt', 'r') as f:
            file_text = f.read()
        return Text(file_text)

    def get_random_sentence(self, length):
        chosen_word = []
        for i in range(length):
            chosen_word.append(random.choice(self.text.split()))
        return " ".join(chosen_word)

    def word_count(self, word):
        return self.text.split(" ").count(word)

    def most_used_word(self):
        if self.most_used:
            return self.most_used

        words = {}
        for word in self.text.split(" "):
           if word in words:
               words[word] += 1
           else:
               words[word] = 1
        print(words)
        count = 0
        word = ""
        for key, value in words.items():
            if value > count:
                count = value
                word = key
        self.most_used = word, count
        return self.most_used

class Text_Modifications(Text):
    def __init__(self, text):
        self.text = text

    def remove_punc(self):
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in self.text:
            if i in punc:
                self.text = self.text.replace(i, "")
        return self.text

    def remove_stopwords(self):
        stopword_list = []
        for line in open("Stopwords.txt"):
            line = line.strip()
            stopword_list.append(line)

        for i in self.text:
            if i in stopword_list:
                self.text = self.text.replace(i, "")
        return self.text


f = open("thestranger.txt")
a= Text_Modifications(f.read())

print(a.remove_punc())

