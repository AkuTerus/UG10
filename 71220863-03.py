def hitung_keliling(kordinat):
    key = list(dict.keys(kordinat))
    
    posA1= kordinat[key[0]][0]
    posA2= kordinat[key[0]][1]
    posB1= kordinat[key[1]][0]
    posB2 = kordinat[key[1]][1]
    posC1 = kordinat[key[2]][0]
    posC2 = kordinat[key[2]][1]
    hitung_jarakAB = (((posA1-posB1)**2)+((posA2-posB2)**2))**0.5 
    hitung_jarakBC = (((posB1-posC1)**2)+((posB2-posC2)**2))**0.5 
    hitung_jarakAC = (((posC1-posA1)**2)+((posC2-posA2)**2))**0.5 
    count_total = hitung_jarakAB+hitung_jarakBC+hitung_jarakAC
    titik = ''
    for i in key :
        titik = titik + i 
    print(f'Segitia {titik} memiliki keliling {count_total:.4f}')  
test = {'A':[1,1],'B':[5,1],'C':[3,7]}
hitung_keliling(test)
test2 = {"J":[1,3], "K":[4,5], "L":[3,0]}
hitung_keliling(test2)