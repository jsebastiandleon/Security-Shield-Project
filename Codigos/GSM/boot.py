
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

def do_connect(SSID='Nombre de la red',password='Contraseña de la red'):
    global wlan
    wlan= network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('conectando a: ', SSID,'...' )
        wlan.connect(SSID,password)
        while not wlan.isconnected():
            pass
    print('configuracion de red:', wlan.ifconfig())

do_connect()
