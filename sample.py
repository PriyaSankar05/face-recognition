from googletrans import Translator,LANGUAGES

sample_text= 'This is my house'

for languages in LANGUAGES:
    t= Translator().translate(sample_text,dest=language)
    print(LANGUAGES[languages] + ':' + t.text)
