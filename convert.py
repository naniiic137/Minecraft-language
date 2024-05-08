# the original t = ℸ ̣
letter={
    'a':'ᔑ',
    'b':'ʖ',
    'c':'ᓵ',
    'd':'↸',
    'e':'ᒷ' ,
    'f':'⎓',
    'g': '⊣',
    'h': '⍑',
    'i': '╎',
    'j':'⋮',
    'k':'ꖌ',
    'l': 'ꖎ',
    'm': 'ᒲ',
    'n':'リ',
    'o': '𝙹',
    'p': '!¡',
    'q': 'ᑑ',
    'r': '∷',
    's': 'ᓭ',
    't': 'ℸ',
    'u' :'⚍',
    'v': '⍊' ,
    'w':'∴',
    'x':' ̇/',
    'y': '||',
    'z': '⨅',
    ' ':' '
}

print(" 1 : minercraft language")
print(" 2 : normal language")
n=input(">>> ")

if n=='1':
    ch=input("something you want to change : ")
    s=''
    for c in ch:
        s=s+letter[c]
    print(s)
else:
    ch=input("something you want to change : ")
    s=''
    for c in ch:
        s=s+list(letter.keys())[list(letter.values()).index(c)]
    print(s)

input()