
# ###  XP
# # Ex - 1
#
# # import json
# # import random
# #
# # def get_words_from_file():
# #     words = []
# #     with open('wordlist.txt','r') as f:
# #         for line in f:
# #             words.append(line.rstrip('\n'))
# #         f.close()
# #         return words
# #
# # def get_random_sentence(length):
# #     sentence = ''
# #     return_words = get_words_from_file()
# #     random_words = random.choices(return_words, k = length)
# #     for word in random_words:
# #         sentence += word + ' '
# #     print(sentence.lower)
# #
# # def sent_length():
# #     num = int(input("Enter a number value for how long your sentence should be: "))
# #     if 2 <= num <= 20:
# #         get_random_sentence(num)
# #     else:
# #         raise Exception("Incorrect value enterred")
# #
# # def main():
# #     print('this exercise we will create a random sentence generator')
# #     print("Would you like to make a random sentence? (yes / no) ")
# #     user_input = input()
# #     if user_input == 'yes':
# #         sent_length()
# #     else:
# #         print("Have a good day.")
# # main()
# import random
# from os import error
#
#
# # import random
# # # num_of_words  = int(input('how many words should be in the sentence? '))
# #
# #
# # def get_words_from_file():
# #     words = []
# #     with open('wordlist.txt', 'r') as f:
# #         for line in f:
# #             words.append(line.rstrip('\n'))
# #         f.close()
# #         return words
# #
# #
# # def get_random_sentence(num):
# #     sentence = ''
# #     get_words = get_words_from_file()
# #     rndm_words = random.choices(get_words, k=num)
# #     for word in rndm_words:
# #         sentence += word+' '
# #     print(sentence.lower())
# #
# #
# # def get_num():
# #     num = input('Enter a number of words should create your sentence: ')
# #     if 2 <= int(num) <= 20:
# #         get_random_sentence(int(num))
# #         main()
# #     else:
# #         SyntaxError
# #         print("wrong number")
# #
# #
# # def main():
# #     print('The program job is to take random words and make a sentence in a length YOU CHOOSE!')
# #
# #
# # get_num()
#
# # Ex-2
#
# # import json
# # sampleJson = {"company": {"employee": {"name": "emma","payable": {"salary": 7000,"bonus": 800}}}}
# #
# #
# # print(sampleJson["company"]["employee"]["payable"]["salary"])
# #
# #
# # sampleJson["company"]["employee"]["birth_date"] = 0
# # print(sampleJson["company"]["employee"])
# #
# #
# #
# # json_file = "jsonfile.json"
# #
# # with open(json_file,'w') as file_obj:
# #     json.dump(sampleJson, file_obj)
