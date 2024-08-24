# from translate import Translator
# from gtts import gTTS
# import os

# def translate_text(text, target_language='hi'):
#     """
#     Translates the given text to the target language using the translate library.
#     :param text: Text to be translated.
#     :param target_language: Target language code (e.g., 'hi' for Hindi, 'es' for Spanish).
#     :return: Translated text.
#     """
#     translator = Translator(to_lang=target_language)
#     translation = translator.translate(text)
#     return translation

# def text_to_speech(text, language='en', output_directory=r"D:\Code\Web Development\project\Full stack\Say it\Python"):
#     """
#     Converts text to speech using gTTS and saves it as an audio file.
#     :param text: Text to be converted to speech.
#     :param language: Language code (e.g., 'en' for English, 'hi' for Hindi).
#     :param output_directory: Directory to save the output audio file.
#     :return: Path to the output audio file.
#     """
#     tts = gTTS(text=text, lang=language)
    
#     # Create a unique filename for each language
#     filename = os.path.join(output_directory, f"output_{language}.mp3")
#     tts.save(filename)
    
#     os.system(f'start "" "{filename}"')  # Opens the file using the default player
#     return filename

# # Main function
# if __name__ == "__main__":
#     # User input for text and language
#     text = input("Enter the text you want to translate and convert to speech: ")
    
#     languages = {
#         'hi': 'Hindi',
#         'es': 'Spanish',
#         'fr': 'French',
#         'de': 'German',
#         'ja': 'Japanese',
#         'gu': 'Gujarati',
#         'zh': 'Chinese'
#     }
    
#     print("Select a language:")
#     for lang_code, lang_name in languages.items():
#         print(f"{lang_code}: {lang_name}")
    
#     target_language = input("Enter the language code from the above list: ")
    
#     if target_language in languages:
#         translated_text = translate_text(text, target_language=target_language)
#         print(f"Translated text: {translated_text}")
#         text_to_speech(translated_text, language=target_language)
#     else:
#         print("Invalid language code selected.")

from translate import Translator
from gtts import gTTS
import os
import sys
import io

def translate_text(text, target_language='hi'):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

def text_to_speech(text, language='en', output_directory=r"D:\Code\Web Development\project\Full stack\Say it\server\audio"):
    tts = gTTS(text=text, lang=language)
    filename = os.path.join(output_directory, f"output_{language}.mp3")
    tts.save(filename)
    os.system(f'start "" "{filename}"')  # Opens the file using the default player
    return filename

if __name__ == "__main__":
    # Ensure stdout uses UTF-8 encoding
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # Arguments passed from Node.js
    if len(sys.argv) < 3:
        print("Please provide both text and target language.")
        sys.exit(1)
    
    text = sys.argv[1]
    target_language = sys.argv[2]

    translated_text = translate_text(text, target_language=target_language)
    print(f"Translated text: {translated_text}")
    text_to_speech(translated_text, language=target_language)
