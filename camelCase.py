'''Noelle this program turns a sentence into camelcase'''

#get a sentence to split 
def main():
    sentence_to_split = input('Enter a sentence and it will be transformed: ')
    conversion = sentence_to_split
sentence_to_split.split()



def conversion(sentence_to_split):
    word_list = sentence_to_split.split()
    new_list = []

    finished_string = ''

    for index, word in enumerate(word_list):
        if index == 0:
            word = word.lower()
        else:
            word = word.lower()
            word_list.append(word)
    return finished_string.join(word_list)
