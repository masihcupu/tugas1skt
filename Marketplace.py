import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:9999")

saldoAwal = 0

class Marketplace(object):
    def topUp(self, amount):
        print (c.transfer(amount))
        global saldoAwal
        saldoAwal = saldoAwal + amount
        return "TopUp berhasil ditambahkan Rp. %s" % saldoAwal

    def Pulsa(self, number, oper, amount):
    	global saldoAwal
    	print (amount)
    	if amount < saldoAwal:
    		saldoAwal = saldoAwal - amount
    		return "Beli pulsa Rp. %s berhasil" %saldoAwal
    	else:
    		return "Saldo Tidak Cukup"

s = zerorpc.Server(Marketplace())
s.bind("tcp://0.0.0.0:10000")
s.run()