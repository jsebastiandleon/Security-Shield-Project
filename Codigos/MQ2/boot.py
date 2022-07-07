
import network
import esp
esp.osdebug(None)

import gc
gc.collect()

def do_connect(SSID='Redmi 9',password='0e6aa3950274'): 
    global wlan
    wlan= network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('conectando a: ', SSID,'...' )
        wlan.connect(SSID,password)
        while not wlan.isconnected():
            pass
    print('configuracion de red:', wlan.ifconfig())

#def do_connect(SSID='J.J.A.B',password='J1962O1966'): 
#   global wlan
    #wlan= network.WLAN(network.STA_IF)
    #wlan.active(True)
    #if not wlan.isconnected():
        #print('conectando a: ', SSID,'...' )
        #wlan.connect(SSID,password)
        #while not wlan.isconnected():
            #pass
    #print('configuracion de red:', wlan.ifconfig())

do_connect()
