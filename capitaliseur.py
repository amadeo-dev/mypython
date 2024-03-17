def capi(mot):
    a = 0
    out =''
    while a < len(mot):
        if a % 2 == 0:
            lettre = mot[a].upper()
        else:
            lettre = mot[a].lower()
        out = out + lettre
        a = a + 1
    return out


print(capi("capitaliseur"))

s = "le petit chaperon rouge est dans la foret."
a = 0
out = ""
while a < len(s):
    if a == 0 or s[a - 1] == ' ':
        out =  out + s[a].upper()
    else:
        out =  out + s[a].lower()
    a = a + 1

print(out)
