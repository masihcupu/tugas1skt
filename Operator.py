import zerorpc
import paho.mqtt.client as mqtt 
import threading
PulsaAnda = 0
verif = 0
def publish():
	threading.Timer(1.0, publish).start()
	global PulsaAnda
	global verif
	if verif == 1:
		mqtt_client = mqtt.Client(client_id="pub1", clean_session=False)
		mqtt_client.connect("localhost", port=1883)
		mqtt_client.publish("/tugas1skt", ("Pulsa anda sekarang "+str(PulsaAnda)), qos=0)
		mqtt_client.disconnect()
		verif = 0

class Operator(object):
	def isi(self, number, oper, amount):
		global PulsaAnda
		global verif
		PulsaAnda = PulsaAnda + amount
		verif = 1
		print("Segera kirim pulsa")

publish()
s = zerorpc.Server(Operator())
s.bind("tcp://0.0.0.0:6969")
s.run()

