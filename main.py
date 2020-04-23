# Assignment 12
# Benjamin Lemery
# 4/24/20
# This program demonstrates various use cases of regular expressions

import re

def regular_expression():
    user_string = input("Enter a string: ")
    user_selection = int(input("Select an option: \n"
                               "Press 1 to see if the string has a 'q'\n"
                               "Press 2 to see if the string contains 'the'\n"
                               "Press 3 to see if the string has a '*' in it.\n"
                               "Press 4 to see if the string contains a digit.\n"
                               "Press 5 to see if the string contains a period\n"
                               "Press 6 to see if the string has at least two consecutive vowels\n"
                               "Press 7 to see if the string contains white space.\n"
                               "Press 8 to see if the string has any letters that repeat three times in a single world.\n"
                               "Press 9 to see if the string starts with the word 'Hello'\n"
                               "Press 10 to see if the string contains an email address.\n"
                               "Press 11 to exit\n"
                               "Press a key: "
                               ))


    # Checks to see if the string has a 'q' in it.
    if user_selection == 1:
        regmatch = re.search(r'[q]', user_string)
        if regmatch:
            print('True: The string has a "q" in it.')
        else:
            print('False: The string does not have a "q" in it.')

    # Checks to see if the string has the word 'the' in it
    elif user_selection == 2:
        regmatch = re.search(r'the', user_string)
        if regmatch:
            print('True: The string has the word "the" in it.')
        else:
            print('False: The string does not have the word "the" in it.')

    # Checks to see if the string has a '*' in it.
    elif user_selection == 3:
        regmatch = re.search(r'[*]', user_string)
        if regmatch:
            print('True: The string has a "*" in it.')
        else:
            print('False: The string has no "*" in it.')

    # Checks to see if the string has a digit in it.
    elif user_selection == 4:
        regmatch = re.search(r'[0-9]', user_string)
        if regmatch:
            print('True: The string has a digit.')
        else:
            print('False: There is no digit in the string.')

    # Checks to see if a string has a period
    elif user_selection == 5:
        regmatch = re.search(r'[.]', user_string)

        if regmatch:
            print('True: The string has a period in it.')
        else:
            print('False: The string has no period in it.')

    # Checks to see if a string has two consecutive vowels
    elif user_selection == 6:
        regmatch = re.search(r'[aeiou]{2}', user_string)
        if regmatch:
            print("True: The string has two consecutive vowels.")
        else:
            print("False: The string does not have two consecutive vowels.")

    # Checks to see if a string has whitespace
    elif user_selection == 7:
        regmatch = re.search(r'[" "]', user_string)
        if regmatch:
            print("True: The string has whitespace.")
        else:
            print("False: The string does not have whitespace.")

    # After trying multiple ideas out I ultimately could not figure this one out. What I'm  thinking is that you have to figure out how to split words apart into temporary strings and now search each temporary string
    # for three repeating characters. This'll identify whether a word has three or more repeating letters and then you can print if any of these temporary strings have 3 or more repeating characters
    # So I got the first part working where it splits the string into seperate words and performs a regular search expression on each individual word returning the results but I could not ultimately identify
    # a way to match 3 consecutive characters specifically efficiently. Theoretically, I could perform a search query for each individual character and do conditional checks on each but this would be painfully inefficient.
    elif user_selection == 8:
        list = user_string.split()
        print(list)
        for i in range (len(list)):
            regmatch = re.search(r'[a-zA-Z]{3}', list[i])
            if regmatch:
                print("True: There are three consecutive letters in a word in this string.")
            else:
                print("False: There are not three consecutive letters in a word in this string.")

    # Checks to see if the string starts with the word "Hello"
    elif user_selection == 9:
        regmatch = re.search("^Hello", user_string)
        if regmatch:
            print('True: The string starts with the word "Hello"')
        else:
            print('False: The word does not start with the word "Hello"')

    # Checks to see if the string contains an email address
    elif user_selection == 10:
        regmatch1 = re.search(r".+@.+.com", user_string)
        regmatch2 = re.search(r".+@.+.edu", user_string)
        regmatch3 = re.search(r".+@.+.org", user_string)
        regmatch4 = re.search(r".+@.+.io", user_string)

        if regmatch1 or regmatch2 or regmatch3 or regmatch4:
            print("True the string contains an email address")
        else:
            print("False: The string does not contain an email address.")

    # Exits the program
    if user_selection != 11:
        regular_expression()
    else:
        print("Exiting the program")
        exit()

regular_expression()
