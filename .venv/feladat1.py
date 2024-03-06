def Euklidesz(a, b):
    while True:
        eredmeny = a % b
        if eredmeny == 0:
            break
        a = b
        b = eredmeny
    print("Az eredmény: ", b)

def KibovitettEuklideszi(a, b):
    x = [1, 0]
    y = [0, 1]
    A, B = a, b
    szamlalo = 1
    while True:
        eredmeny = a % b
        tarolo = a // b
        if eredmeny == 0:
            break
        x.append(tarolo * x[szamlalo] + x[szamlalo-1])
        y.append(tarolo * y[szamlalo] + y[szamlalo-1])
        szamlalo += 1
        a = b
        b = eredmeny
    X = (-1)**szamlalo * x[-1]
    Y = (-1)**(szamlalo+1) * y[-1]
    LNKO = A * X + B * Y
    print(f"Az egyenlet {A*X} + {B*Y}")
    print(f"x értékei: {x}")
    print(f"y értékei: {y}")
    print("A legnagyöbb közös osztó: ",LNKO)


if __name__ == '__main__':
    #Euklidesz(50,16)
    KibovitettEuklideszi(845,68)