'''Noelle this program attempts to turn a sentence into camelcase, its not quite right'''

#get a sentence to split 
def main():
    sentence_to_split = input('Enter a sentence and it will be transformed: ')
    conversion(sentence_to_split)
    sentence_to_split.split()
def conversion(sentence_to_split):
    word_list = sentence_to_split.split()
    new_list = []

    finished_string = ''
    #for loop Nate helped with this in breakout rooms, Im still not sure about it.
    for index, word in enumerate(word_list):
        if index == 0:
            word = word.lower()
        else:
            word = word.capitalize()
            new_list.append(word)
            # return the list of words
    return finished_string.join(new_list)


main()