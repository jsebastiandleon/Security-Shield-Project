#REMEMBER TO RENAME FILE TO main.py BEFORE UPLOAING TO THE BOARD


from utelegram import Bot
from MQ2 import MQ2
from utime import sleep
from machine import Pin, ADC, UART

#Configuracion de Telegram
TOKEN = 'Inserte el token del bot'
bot = Bot(TOKEN)
id=11111111

#Configurando MQ2
pin = Pin(35, Pin.IN)     
sensor = MQ2(pinData = pin, baseVoltage = 3.3)


#Comandos de telegram
@bot.add_command_handler('help')
def help(update):
    update.reply('Escibe gas para ver las lecturas de metano y humo \nEscribe cámara para tomar una foto y visualizarla \nEscribe puerta para ver el estado de la puerta \nEscribe 123 para llamar a emergencias')


@bot.add_message_handler('^gas|Gas|GAS$')
def gas(update):
     MQ2_lecture()

#Funciones del sensor MQ2

def MQ2_lecture():

    bot.send_message(chat_id=id, text='Por favor esperar  ya que el proceso puede tomar alrededor de 10 segundos')
    bot.send_message(chat_id=id, text='El nivel de gas metano en este momento es de: {0}'.format(sensor.readMethane()) + ' ppm')
    bot.send_message(chat_id=id, text='El nivel de humo en este momento es de: {0}'.format(sensor.readSmoke()) + ' ppm')
    
    if sensor.readMethane() < 5300 and sensor.readSmoke() < 550:
            bot.send_message(chat_id=id, text='No te preocupes! es seguro respirar :)')
    elif 5300 <= sensor.readMethane() < 10000:
            bot.send_message(chat_id=id, text='Niveles nocivos de gas para una exposición de hasta 8 horas')
            bot.send_message(chat_id=id, text='Se recomienda revisar una posible fuga')
    elif 10000 <= sensor.readMethane() < 50000:
            bot.send_message(chat_id=id, text='Niveles nocivos de gas para una exposición de hasta 1 hora')
            bot.send_message(chat_id=id, text='Se recomienda revisar en caso de fuga')
    elif 50000 <= sensor.readMethane() < 150000:
            bot.send_message(chat_id=id, text='Niveles nocivos de gas para una exposición de hasta 30 min')
            bot.send_message(chat_id=id, text='Se recomienda actuar rápido para reducir la fuga')
            bot.send_message(chat_id=id, text='No prender un encendedor, luces, y evitar conectar y/o utilizar electrodomésticos')
    elif sensor.readMethane() >= 150000:
            bot.send_message(chat_id=id, text='Niveles nocivos de gas para una exposición de hasta 15 min')
            bot.send_message(chat_id=id, text='Se recomienda evacuar el lugar y arreglar la fuga lo antes posible')
    
    if 550 <= sensor.readSmoke() < 600:
            bot.send_message(chat_id=id, text='Niveles nocivos de humo para una exposición de hasta 8 horas')
            bot.send_message(chat_id=id, text='Se recomienda revisar en caso de posibles problemas')
    elif 600 <= sensor.readSmoke() < 800:
            bot.send_message(chat_id=id, text='Niveles nocivos de humo para una exposición de hasta 1 hora')
            bot.send_message(chat_id=id, text='Se recomienda revisar en caso de problemas')
    elif 800 <= sensor.readSmoke() < 1000:
            bot.send_message(chat_id=id, text='Niveles nocivos de humo para una exposición de hasta 30 min')
            bot.send_message(chat_id=id, text='Se recomienda actuar rápido para reducir los efects nocivos')
    elif sensor.readSmoke() >= 1000:
            bot.send_message(chat_id=id, text='Niveles nocivos de humo para una exposición de hasta 15 min')
            bot.send_message(chat_id=id, text='Se recomienda evacuar el lugar y ventilar el ambiente lo antes posible')
					


def MQ2_alert():
    if 5300 <= sensor.readMethane() < 10000:
        bot.send_message(chat_id=id, text='Alerta! Niveles de gas nocivos, actuar en menos de 8 horas')
        bot.send_message(chat_id=id, text='Lectura: {0}'.format(sensor.readMethane()) + ' ppm')
    elif 10000 <= sensor.readMethane() < 50000:
        bot.send_message(chat_id=id, text='Alerta! Niveles de gas nocivos, actuar en menos de 1 hora')
        bot.send_message(chat_id=id, text='Lectura: {0}'.format(sensor.readMethane()) + ' ppm')
    elif 50000 <= sensor.readMethane() < 150000:
        bot.send_message(chat_id=id, text='Alerta! Niveles de gas nocivos, actuar en menos de 30 min')
        bot.send_message(chat_id=id, text='Lectura: {0}'.format(sensor.readMethane()) + 'ppm')
    elif sensor.readMethane() >= 150000:
        bot.send_message(chat_id=id, text='Alerta! Niveles de gas nocivos, actuar en menos de 15 min')
        bot.send_message(chat_id=id, text='Lectura: {0}'.format(sensor.readMethane()) + 'ppm')
    
    if 550 <= sensor.readSmoke() < 600:
        bot.send_message(chat_id=id, text='Alerta! Niveles de humo nocivos, actuar en menos de 8 horas')
        bot.send_message(chat_id=id, text='Lectura: {0}'.format(sensor.readSmoke()) + 'ppm')
    elif 600 <= sensor.readSmoke() < 800:
        bot.send_message(chat_id=id, text='Alerta! Niveles de humo nocivos, actuar en menos de 1 hora')
        bot.send_message(chat_id=id, text='Lectura: {0}'.format(sensor.readSmoke()) + 'ppm')
    elif 800 <= sensor.readSmoke() < 1000:
        bot.send_message(chat_id=id, text='Alerta! Niveles de humo nocivos, actuar en menos de 30 min')
        bot.send_message(chat_id=id, text='Lectura: {0}'.format(sensor.readSmoke()) + 'ppm')
    elif sensor.readSmoke() >= 1000:
        bot.send_message(chat_id=id, text='Alerta! Niveles de humo nocivos, actuar en menos de 15 min')
        bot.send_message(chat_id=id, text='Lectura: {0}'.format(sensor.readSmoke()) + ' ppm')


        

def main ():
    sensor.calibrate()
    print("Calibration completed")
    print("Base resistance:{0}".format(sensor._ro))
    while True:
        MQ2_alert()

        


            
            

bot.start_loop(main, ())


