# -*- coding: utf-8 -*-

# Program cw3_34
# Program oblicza N-ty wyraz ciągu Fibonacciego

if __name__ == "__main__":
    n = int(input("Podaj ktory wyraz ciągu Fibonacciego ma zostac wyliczony: "))

    if n < 0:
        print("Podana liczba musi być >=0")
    else:
        if n == 0:
            print(f"")
