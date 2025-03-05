from googletrans import Translator


def translate_text(text, src, dest):
    # Initialize the Translator
    translator = Translator()

    # Translate the text between the chosen languages
    translation = translator.translate(text, src=src, dest=dest)

    # Return the translated text
    return translation.text


if __name__ == '__main__':
    # Create a loop to keep asking for input
    while True:
        # Ask the user to choose the direction of translation
        print("\nSelect translation mode:")
        print("1. English to Arabic")
        print("2. Arabic to English")
        print("Type 'exit' to quit.")

        choice = input("Enter your choice (1 or 2): ").strip().lower()

        # Check if the user wants to exit the loop
        if choice == 'exit':
            print("Exiting the translation tool. Goodbye!")
            break

        if choice == '1':
            src_lang = 'en'
            dest_lang = 'ar'
        elif choice == '2':
            src_lang = 'ar'
            dest_lang = 'en'
        else:
            print("Invalid choice, please select either 1 or 2.")
            continue

        # Input text from the user to translate
        text_to_translate = input(f"Enter the text to translate ({src_lang} -> {dest_lang}): ")

        try:
            # Translate the input text
            translated_text = translate_text(text_to_translate, src_lang, dest_lang)
            print(f"Translated Text ({dest_lang}): {translated_text}\n")
        except Exception as e:
            # Handle any errors that occur during translation
            print(f"Error during translation: {str(e)}")
