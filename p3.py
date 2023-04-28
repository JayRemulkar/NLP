# Write a program to Implement a tri-gram model

from nltk import word_tokenize
from nltk.util import ngrams
from sys import exit

def main():
    text = "This is a sample text corpus for N-gram language model implementation."
    
    WArr = word_tokenize(text)      # making list of words
                #   list  n 
    trigram = ngrams(WArr,3)        # trigram 
    
    for elm in trigram:
        print(elm)

if __name__ == "__main__":
    main() 