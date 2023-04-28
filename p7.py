# Write a program to Implement Named Entity Recognition (NER)

import spacy

def main():
    nlp = spacy.load("en_core_web_sm")

    text = "Nitin is studying at Indian Instute of technology Bombay."

    doc = nlp(text)

    for entity in doc.ents:
        print(entity.label_, entity.text)

if __name__ == "__main__":
    main()