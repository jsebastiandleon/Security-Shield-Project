#REMEMBER TO RENAME FILE TO main.py BEFORE UPLOAING TO THE BOARD

from utelegram import Bot
import utime
import machine 

#Configuracion de Telegram
TOKEN = '5596407792:AAFey_P4G1gq7b4excdBUiCXGgILoHW449Q'
bot = Bot(TOKEN)
id=2005590886

#Configurando el SIM800L
gsm = machine.UART(2, 115200)
   
        
#Comandos de telegram
@bot.add_command_handler('help')
def help(update):
    update.reply('Escibe gas para ver las lecturas de metano y humo \nEscribe cámara para tomar una foto y visualizarla \nEscribe puerta para ver el estado de la puerta \nEscribe 123 para llamar a emergencias')


@bot.add_message_handler('^123$')
def emergencias(update):
     sim800l()

#Funciones del SIM800L

def sim800l():
    gsm.write('AT+CMGF=1\r')
    utime.sleep(2)
    gsm.write('AT+CMGS="+123"\rLlamando a emergencias\r')
    utime.sleep(2)
    gsm.write('\x1A')
    gsm.read()
    gsm.read()
    bot.send_message(chat_id=id, text='Llamando a emergencias')

        



        

bot.start_loop()



