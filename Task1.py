print("Task 1, podaj cyfrę/y w przedziale 32-bitowym, które program odwróci")
N = int(input("Input: "))

#Bit oraz BitNeg zakreślaja przedział 32 bitowych liczb
bit = 2147483647
bit_neg = -2147483648

#sprawdza czy liczba jest 32 bitowa
if N <= bit and (N >= bit_neg):
    if N < 0:
        N = N * -1
        N = str(N)[::-1]
        print("Output: ", int(N) * -1)
    else:
        print("Output: ", str(N)[::-1])
else:
    print(0)