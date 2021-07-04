def main():
    '''Main function'''
    string = input("Text: ")
    letters = count_letters(string)
    words = count_words(string)
    sentences = count_sentences(string)

    L = letters * (100 / words)
    S = sentences * (100 / words)

    grade = round(0.0588 * L - 0.296 * S - 15.8)
    
    if grade < 1:
        print("\nBefore Grade 1")
    elif grade > 15:
        print("\nGrade 16+")
    else:
        print(f"\nGrade {grade}")
        
    print(f"\nLetters: {letters}\nWords: {words}\nSentences: {sentences}\n")


def count_letters(string):
    '''Helper function that accepts a string and returns a letter count'''
    letters = 0
    for char in string:
        if (char.isalpha()) == True:
            letters += 1
    return letters

def count_words(string):
    '''Helper function that accepts a string and returns a word count'''
    words = 1
    prev_char = ""
    for char in string:
        if (char != " ") and (prev_char == " "):
            words += 1
        prev_char = char
    return words

def count_sentences(string):
    '''Helper function that accepts a string and returns a sentence count'''
    punctuation = [".", "?", "!"]
    sentences = 1
    prev_char = ""
    for char in string:
        if (char not in punctuation) and (char != '"') and (prev_char in punctuation):
            sentences += 1
        prev_char = char
    return sentences

main()