from nrclex import NRCLex


def nrcdectect(text):
    emotion = NRCLex(text)
    feel=emotion.top_emotions
    return feel



