def hitung_nilai_akhir(daftar_nilai,n):
    daftarnama_sorted=sorted(daftar_nilai)
    daftar_nilai = {key:daftar_nilai[key]for key in daftarnama_sorted}
    for nama in daftar_nilai:
        nilai_list  = []
        for i in daftar_nilai[nama]:
            nilai_list.append(i)
        nilai_list.sort(reverse=True)
        total = 0
        for j in range(n):
            total = total+nilai_list[j]
        print(f'Nilai {nama} : {total/n:.6f}')
daftar_nilai = {
    'Udin' : [65, 74, 56, 80, 82, 94],
    'Atun' : [98, 84, 82, 88],
    'Tejo' : [85, 86]
}
hitung_nilai_akhir(daftar_nilai, 2)