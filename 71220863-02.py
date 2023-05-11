#ini nomor 2
def total_tanpa_tigabelas(list_angka):
    total = 0
    if len(list_angka)==0:
        return ('Isi List Kosong')
    else:
        for i in range(len(list_angka)):
            total = total+list_angka[i]
            if list_angka[i]==13:
                total=total-13
                break
        return total

print(total_tanpa_tigabelas(([2,4,1,3,13,8])))
print(total_tanpa_tigabelas(([])))


