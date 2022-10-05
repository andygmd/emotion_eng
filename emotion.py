import translators as ts
from nrclex import NRCLex


def nrcdectect(text):
    emotion = NRCLex(text)
    feel=emotion.top_emotions
    return feel


def transform(text):
    translation=ts.google(text, from_language='zh-TW', to_language='en')
    return nrcdectect(translation)

#transform('我好開心')