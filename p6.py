# Write a program to Implement dependency parsing of a given text

import nltk
import spacy
from spacy import displacy 

def main():
    nlp = spacy.load("en_core_web_sm") #nlp model

    text = "John likes Mary because she is beautiful."

    doc = nlp(text)

    for token in doc:
        print(token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children])

if __name__ == "__main__":
    main()