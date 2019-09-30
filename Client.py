import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:10000")

print ("Menu :")
print ("1. TopUp Saldo")
print ("2. Beli Pulsa")
pilih = input()
pilih = int(pilih)
if pilih == 1:
	print ("Masukkan Nilai TopUp")
	amount = input()
	print ("Apakah sudah yakin ? y/n")
	bool=input()
	if bool == "y":
		print (c.topUp(int(amount)))
	else:
		print ("Ok ok kalo gak jadi")
if pilih == 2:
	print ("Masukkan Nomer HP")
	number = input()
	print ("Nama Operator")
	oper = input()
	print ("Jumlah pulsa")
	amount = input()
	print ("Apakah sudah yakin ? y/n")
	bool=input()
	if bool == "y":
		print (c.Pulsa(number, oper, int(amount)))
	else:
		print ("Ok ok kalo gak jadi")
else:
	print("Belum ada fiturnya boss")