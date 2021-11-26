class Anagram_checker():
    def __init__(self):
        with open("sowpods.txt") as f:
            self.word_list = [word.strip() for word in f]
        self.results = {}

    def get_word(self):
        flag = True
        while flag:
            word = input("Please enter a word and I'll tell you its anagrams: ").upper()
            print(word)
            if word in self.word_list:
                self.results[word] = []
                return word
            else:
                print("This is not a real word. Try again.")

    def get_anagrams(self, word1):
        for word2 in self.word_list:
            self.is_anagram(word1, word2)

    def is_anagram(self, word1, word2):
        w1_list = list(word1)
        w1_list.sort()
        w2_list = list(word2)
        w2_list.sort()
        if (w1_list == w2_list):
            self.results[word1].append(word2)

    def play(self):
        self.get_anagrams(self.get_word().upper())