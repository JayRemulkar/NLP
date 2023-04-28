# Write a program to implement sentence segmentation and word tokenization.

from nltk import sent_tokenize,word_tokenize

def main():
    phara = "Backgammon is one of the oldest known board games. Its history can be traced back nearly 5,000 years to archeological discoveries in the Middle East. It is a two player game where each player has fifteen checkers which move between twenty-four points according to the roll of two dice."

    # Sentence Segmentation 
    sentences = sent_tokenize(phara)
    for sentence in sentences:
        print(sentence+"\n")

    # word Tokenization
    for sentence in sentences:
        words = word_tokenize(sentence)
        print(words)

if __name__ == "__main__":
    main()