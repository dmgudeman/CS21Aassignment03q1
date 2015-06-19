# -----------------------------------------------------------------------------
# Name:        spam
# Purpose:     Classify text input as SPAM or HAM
#
# Author:      David Gudeman
# Date:        June 18, 2015
# -----------------------------------------------------------------------------
"""
Enter your module docstring with a one-line overview here

and a more detailed description here.
"""
import string
SPAM_WORDS = {'opportunity', 'inheritance', 'money', 'rich', 'dictator',
              'discount', 'save', 'free','offer', 'credit',
              'loan', 'winner', 'warranty', 'lifetime', 'medicine',
              'claim', 'now', 'urgent', 'expire', 'top',
              'plan', 'prize', 'congratulations', "help", "widow"}

def spam_indicator(input_message):
    """
    Enter your function docstring here
    """
    # this function returns the spam indicator rounded to two decimals
    input_message = "".join(c for c in input_message
                            if c not in string.punctuation)
    input_message = input_message.lower()
    input_words = set(input_message.split())

    print(input_words)
def classify(indicator):
    """
    Enter your function docstring here
    """
    # this function prints the spam classification

def get_input():
    """
    Obtain the input from the user
    prompt the user for input until they enter a non-empty string
    return the string entered by the user

    """
    message = str(input('Please enter your message:'))
    while message == "":
        message = str(input('Please enter your message:'))
    return message

def main():
    # get the user input and save it in a variable
    # Call spam_indicator to compute the spam indicator
    # Print the spam_indicator
    # Call classify to print the classification

    input_message = get_input()
    print(input_message)
    spam_indicator(input_message)
if __name__ == '__main__':
    main()