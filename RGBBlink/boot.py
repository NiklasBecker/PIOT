# boot.py -- run on boot-up
from network import WLAN
import machine
wlan = WLAN(mode=WLAN.STA)

wlan.connect(ssid='AndroidAP292C', auth=(WLAN.WPA2, 'olpo7642'))
while not wlan.isconnected():
    machine.idle()
print("WiFi connected successfully")
print(wlan.ifconfig())