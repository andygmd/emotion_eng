import text2emotion as te
def csta(ans):
    if ans!="Happy" and ans!="Surprise":
        return "negative"
    else:
        return "positive"
    

def texdectect(text):
    feel=te.get_emotion(text)
    ans=""
    cal=0
    for i in feel:
        if feel[i]>=cal:
            cal=feel[i]
            ans=i
    stage=csta(ans)
    return [ans,feel[ans],stage]
