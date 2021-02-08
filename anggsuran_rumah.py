def tipe_rumah(tipe):
    dp = 20*(tipe/100)
    print("Dp yang harus dibayar minimal Rp : {:,}".format(int(dp)))

    valid = True
    while(valid):
        try:
            print("jumlah dp yang akan di bayar ")
            dp_rumah = int(input("isi tanpa titik atau koma, contoh-> 6000000 : "))
            if(dp_rumah < dp):
                print("pembayaran dp minimal {}".format(dp))
                valid = True
            else:
                valid = False
        except:
            print("nilai dp harus berupa angka")
    bayar_dp = tipe - dp_rumah

    valid1 = True
    while (valid1):
        try:
            anggsuran = int(input("lama angsuran (11/18/24) Bulan : "))
            if (anggsuran ==11 or anggsuran ==18 or anggsuran == 24):
                bayar_anggsuran = bayar_dp / anggsuran
                bayar_anggsuran = round(bayar_anggsuran)
                print("jumlah pembayaran setiap bulan selama {} bulan adalah Rp {:,}".format(anggsuran, bayar_anggsuran))
                valid1 = False
            else:
                print("{} tidak ada dalam angsuran".format(anggsuran))
                valid1=True
        except:
            print("nilai anggsuran harus berupa angka")

print("Type Rumah \t Harga")
print("    A      \t 120.000.000")
print("    B      \t 110.000.000")
print("    c      \t 100.000.000")
print()

validasi = True
while (validasi):
    type_rumah = input("Pilih type Rumah : ")
    print()
    print("anda memilih type rumah {}".format(type_rumah))

    type_a = 120000000
    type_b = 110000000
    type_c = 100000000

    if (type_rumah.upper() =="A"):
        tipe_rumah(type_a)
        validasi=False

    elif (type_rumah.upper() =="B"):
        tipe_rumah(type_b)
        validasi=False

    elif (type_rumah.upper() =="C"):
        tipe_rumah(type_c)
        validasi=False
    else:
        print("type rumah tidak ada dalam pilihan")
        validasi = True