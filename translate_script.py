from translate import Translator

translator = Translator(to_lang="hi")

with open("file1.txt", "r") as f:
    english_text = f.read()

hindi_text = translator.translate(english_text)

with open("file2.txt", "w", encoding="utf-8") as f:
    f.write(hindi_text)
