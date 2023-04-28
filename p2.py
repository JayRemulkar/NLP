# Write a program to Implement stemming and lemmatization.

from nltk.stem import PorterStemmer,WordNetLemmatizer
# nltk.download('punkt')
# nltk.download('wordnet')

def main():
    WArr = ["run","runner","running","ran","runs","easily","fairly"]
    Sout,Lout = list(),list()

    # Stemming 
    PS = PorterStemmer()
    for word in WArr:
        Sout.append(PS.stem(word))

    # Lemmatization
    LM = WordNetLemmatizer()
    for word in WArr:
        Lout.append(LM.lemmatize(word))

    print("Original Words : ",WArr)
    print("After Stemming : ",Sout)
    print("After Lemmatizition : ",Lout)

if __name__ == "__main__":
    main()