def make_sentence(word, part_of_speech):
    """
    Depending on the part_of_speech value, constructs and prints a sentence using the word.
    - 0 for noun
    - 1 for verb
    - 2 for adjective
    """
    if part_of_speech == 0:
        # Noun case: using template for noun
        print("I am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speech == 1:
        # Verb case: using template for verb
        print("It's so nice outside today it makes me want to " + word + "!")
    elif part_of_speech == 2:
        # Adjective case: using template for adjective
        print("Looking out my window, the sky is big and " + word + "!")
    else:
        # If the part_of_speech is invalid
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    # Taking the word input
    word = input("Please type a noun, verb, or adjective: ")
    
    # Asking the user for part of speech
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    
    # Call the function to print the sentence
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
