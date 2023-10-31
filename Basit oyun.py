import random

def main():
    # Oyun tahtasını oluştur
    tahta = [[random.randint(0, 2) for _ in range(4)] for _ in range(4)]

    # Oyunu başlat
    while True:
        # Oyun tahtasını göster
        print_board(tahta)

        # Hareketi al
        hareket = input("Hareketi girin (yukarı, aşağı, sola, sağa): ")

        # Hareketi uygula
        tahta = hareket_yap(tahta, hareket)

        # Oyun bitti mi?
        if oyun_bitti(tahta):
            print("Oyun bitti!")
            break

def print_board(tahta):
    for satir in tahta:
        print(" ".join([str(rakam) for rakam in satir]))

def hareket_yap(tahta, hareket):
    if hareket == "yukarı":
        tahta = tahta[::-1]
        tahta = birlestir(tahta)
        tahta = tahta[::-1]
    elif hareket == "aşağı":
        tahta = tahta[::1]
        tahta = birlestir(tahta)
        tahta = tahta[::1]
    elif hareket == "sola":
        tahta = tahta.transpose()
        tahta = birlestir(tahta)
        tahta = tahta.transpose()
    elif hareket == "sağa":
        tahta = tahta.transpose()[::-1]
        tahta = birlestir(tahta)
        tahta = tahta.transpose()[::-1]
    else:
        print("Geçersiz hareket!")
        return tahta

    return tahta

def birlestir(tahta):
    for satir in range(4):
        for sutun in range(3):
            if tahta[satir][sutun] == tahta[satir][sutun + 1] and tahta[satir][sutun] != 0:
                tahta[satir][sutun] *= 2
                tahta[satir][sutun + 1] = 0
    return tahta

def oyun_bitti(tahta):
    for satir in range(4):
        for sutun in range(3):
            if tahta[satir][sutun] == 0 or (tahta[satir][sutun] == tahta[satir][sutun + 1] and tahta[satir][sutun] != 0):
                return False
    return True

if __name__ == "__main__":
    main()