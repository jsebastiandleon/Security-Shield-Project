#REMEMBER TO RENAME FILE TO main.py BEFORE UPLOAING TO THE BOARD

from utelegram import Bot
from utime import sleep
from machine import Pin

#Configuracion de Telegram
TOKEN = 'Inserte el token del bot'
bot = Bot(TOKEN)
id=11111111

#Configuracion Reed switch
reed = Pin(19, Pin.IN, Pin.PULL_UP)
   
        
#Comandos de telegram
@bot.add_command_handler('help')
def help(update):
    update.reply('Escibe gas para ver las lecturas de metano y humo \nEscribe cámara para tomar una foto y visualizarla \nEscribe puerta para ver el estado de la puerta \nEscribe 123 para llamar a emergencias')


@bot.add_message_handler('^puerta|Puerta|PUERTA$')
def puerta(update):
    reed_lecture()

#Funciones del sensor reed

def reed_lecture():
    if reed.value():
        bot.send_message(chat_id=id, text='La puerta esta abierta')
    else:
        bot.send_message(chat_id=id, text='La puerta esta cerrada')

def reed_alert():
    if reed.value():
        bot.send_message(chat_id=id, text='La puerta esta abierta')

        
def main ():
    while True:
        reed_alert()
        sleep(5)


        

bot.start_loop(main, ())



