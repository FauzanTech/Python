db = {
"Mie instan" : "4000", 
"Minyak goreng /Liter" : "28.000",
"Tepung terigu /Kg" : "17.000",
"Sabun mandi batang" : "5000",
"Shampo Sachet" : "1.000",
"Deterjen Sachet": "6.000",
"Pasta Gigi" : "10.000",
"Sikat Gigi" : "4.000",
"Beras /Kg" : "10.000",
"Telur" : "2.000",
"Sirup" : "12.000",
"Gula pasir /Kg" : "10.000",
"Teh Sachet" : "5.000",
"Kopi Sachet" : "3.000",
"SKM" : "7.000",
"Mentega" : "8.000",
"Sabun cuci piring" : "12.000",
"Kecap" : "10.000",
"Sambal" : "10.000",
"Air mineral 600ml" : "4.000"
}

for i,k in enumerate(db):
    jarak = 20 - len(k)
    spasi = " "
    index = str(i+1)+" " if i+1 < 10 else i+1
    print(f"{index}. Barang {k}{spasi*jarak}| \n\tHarga Rp.{db[k]}")