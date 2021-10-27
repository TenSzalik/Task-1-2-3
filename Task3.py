import textwrap
import re

text_input = str(input("Wpisz tekst do wyjustowania: "))
text_width = int(input("Maksymalna długość tekstu: "))

wrapper = textwrap.TextWrapper(width=text_width)
dedented_text = textwrap.dedent(text=text_input)

list = []
txt = wrapper.fill(text=dedented_text)

#funkcja justująca
def justify(txt:str, width:int) -> str:
    prev_txt = txt
    while((l:=width-len(txt))>0):
        #przypisywanie txt wyrażeń regularnych
        txt = re.sub(r"(\s+)", r"\1 ", txt, count=l)
        if(txt == prev_txt):
            break
    #dodawanie do listy oosbnych elementów
    list.append(txt.ljust(width))
    return txt.ljust(width)

for l in txt.splitlines():
    justify(l, text_width)
    #print(justify(l, text_width)) <-- sam ciąg znaków wyciągnięty z listy

k = 0
#wyświetlanie tekstu w liście
print("Output: ")
while k < len(list):
    print(list[k:k+1])
    k += 1
