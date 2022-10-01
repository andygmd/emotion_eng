import NRC,tex
def emo(text):
    ncrl=NRC.nrcdectect(text)
    te=tex.texdectect(text)
    ans=[]
    if ncrl[0][0]==te[2]:
        ans.append(te[2],end=" ")
        if len(ncrl)>1:
            ans.append (ncrl[1][0])
        else:
            ans.append(te[0])
    else :
        ans.append("undefined")