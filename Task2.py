print("Task2, podaj cyfrę/y od 1 do 9 by wygenerować wszystkie możliwe kombinacje numerów telefonów")
num = str(input("Input: "))

dic = {"1": "",
       "2": "a" "b" "c",
       "3": "d" "e" "f",
       "4": "g" "h" "i",
       "5": "j" "k" "l",
       "6": "m" "n" "o",
       "7": "p" "q" "r" "s",
       "8": "t" "u" "v",
       "9": "w" "x" "y" "z",
}

y = 0
x = 0
b = 0
k = 0
d = 0
combinations = []

#zapętlaj dopóki y (0) nie będzie równe dłogości input num
while y < len(num):
    #jeśli podany numer ma tylko jeden znak
    if len(num) == 1:
        #jeśli podany numer jest równy 1
        if int(num[y]) == 1:
            break
        else:
            while d < len(dic[num[y]]):
                combinations.append(dic[num[y]][d])
                d += 1
            break
    #jeśli podany numer ma więcej niż 1 znak
    else:
        #pobieraj kolejne wartości z INPUTA num po kolei
        get_figure = num[y]
        try:
            get_figure2 = num[y + 1]
        except IndexError:
            break
        #pobierz litery z tabeli dic
        get_dic = dic[get_figure]
        get_dic2 = dic[get_figure2]
        #operowanie na 3/4 literach z wartości z tabeli
        while x < len(get_dic):
            #operowanie na następnej literze
            while b < len(get_dic2):
                combinations.append(get_dic[x] + get_dic2[b])
                b += 1
                if b == len(get_dic2):
                    b = 0
                    break
            x += 1
            if x == len(get_dic2):
                x = 0
                break
        y += 1

print("Output: ", combinations)