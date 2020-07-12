from google.cloud import translate_v2 as translate
import os
import six
import codecs
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=os.path.join(os.getcwd(), 'translate-dbde36d71c4c.json')
translate_client = translate.Client()
f = open("zgs.txt",encoding='utf-8')
text = f.read()
target = 'en'

if isinstance(text, six.binary_type):
    text = text.decode('utf-8')

# Text can also be a sequence of strings, in which case this method
# will return a sequence of results for each text.
result = translate_client.translate(
    text, target_language=target)

print(u'Text: {}'.format(result['input']))
print(u'Translation: {}'.format(result['translatedText']))
print(u'Detected source language: {}'.format(
    result['detectedSourceLanguage']))
f.close()