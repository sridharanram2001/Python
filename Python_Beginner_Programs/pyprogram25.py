def break_words(stuff):
        ''' This function will break up words '''
        words=stuff.split(' ')
        return words
def sort words(words):
        ''' Sorts the words separately and places in a list '''
        return sorted(words)

def print_first_word(words):
 ''' Prints the first word after popping if off '''      
      word=words.pop(0)
       print(word)

def sort_sentence(sentence):
  ''' Prints the last word after popping if off '''
      word=words.pop(-1)
       print(word)

def print_first_and_last(sentence):
    words=break_words(sentence)
    print_first_word(words)
    print_last_words(words)

def first_first_and_last_sorted(sentence):
    ''' Sorts teh words and prints the first and last words '''
    words=sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)






 