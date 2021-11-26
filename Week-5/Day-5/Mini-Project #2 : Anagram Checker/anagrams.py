from anagram_checker import Anagram_checker
def main():
    new_anagram = Anagram_checker()
    show_menu(new_anagram)


def show_menu(object):
    flag = True
    while flag:
        menu_choice = input('''
Menu:
(e) Enter a word 
(x) Exit  ''').lower()
        if menu_choice == "e":
            object.play()
        elif menu_choice == "x":
            print_results(object)
            flag = False
        else:
            print("Invalid word. Try again. ")

def print_results(object):
    print("The anagrams we found today were: \n")
    for k, v in object.results.items():
        print(f"{k}:{v}")

main()