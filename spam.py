# -----------------------------------------------------------------------------
# Name:        spam
# Purpose:     Classify text input as SPAM or HAM
#
# Author:      David Gudeman
# Date:        June 18, 2015
# -----------------------------------------------------------------------------
"""
Program parses text into words and classifies them as SPAM or HAM

It queries the user for input. It compares the words in the input text
to a list of SPAM words reqardless of punctuation or case. It then
determines the frequency of unique SPAM words. If SPAM words are greater
than 10% of the words it the text is classified as SPAM, otherwise it is HAM.
"""
import string
SPAM_WORDS = {'opportunity', 'inheritance', 'money', 'rich', 'dictator',
              'discount', 'save', 'free','offer', 'credit',
              'loan', 'winner', 'warranty', 'lifetime', 'medicine',
              'claim', 'now', 'urgent', 'expire', 'top',
              'plan', 'prize', 'congratulations', "help", "widow"}
THRESHOLD = 0.1

def spam_indicator(input_message):
    """
    Strips text of punctuation and converts it to lowercase. The parses
    it into words and compares those words to the SPAM_WORDS list. It
    prepares a ratio of SPAM to total words.

    parameter: text - the input message
    returns: float - rounded to two decimals
    """
    input_spam = set()              # initialize an empty set

    # strip the input message of punctuation
    input_message = "".join(c for c in input_message
                            if c not in string.punctuation)
    input_message = input_message.lower() # convert message to lowercase

    # parse message to words and store in a set to filter out duplicates
    input_words = set(input_message.split())
    for word in input_words:     # iterate through the set
        if word in SPAM_WORDS:   # comparing it to SPAM word list
            input_spam.add(word) # matches stored in previously intialized set

    indicator = len(input_spam) / len(input_words) # prepare SPAM/total ratio
    indicator = round(indicator, 2)                # round to 2 decimals

    return indicator             # make available to next function

def classify(indicator):
    """
    Takes the SPAM/total ratio and classifies the input text as SPAM or HAM.
    Prints out the results.

    parameter: float - the SPAM/total ratio, indicator
    prints out: ratio, and SPAM-or-HAM classification
    """
    print('SPAM indicator: ', indicator)    # print out ratio
    if indicator > THRESHOLD:               # threshold for SPAM or HAM
        print('This message is: SPAM')      # prints out the evaluation
    else:
        print('This message is: HAM')

def get_input():
    """
    Obtain the input from the user

    prompts: the user for input until they enter a non-empty string
    returns: the string entered by the user
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
    indicator = spam_indicator(input_message)
    classify(indicator)

if __name__ == '__main__':
    main()