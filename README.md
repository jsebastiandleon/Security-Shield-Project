# Security-Shield-Project

## Integrantes

- Cristian Javier Acosta Duarte
- Julio Sebastián Díaz León
- Daniel Alejandro Gaspar Montaño
- Julián Andrés Silva Cuadros

## Descripción Breve del Proyecto

<p align="center">
<img src="https://user-images.githubusercontent.com/82488285/160315305-e79598b7-f2be-41a3-8f1d-776e9a1b26a6.png" width="600">
</p>

Security Shield Crew es un proyecto de domótica orientado a la seguridad en un hogar, compuesto por un sistema embebido modular que permite la verificación del estado de seguridad del lugar. Está compuesto por cuatro módulos, cada uno orientado a la detección, procesamiento y alerta de eventos riesgosos que puedan comprometer la seguridad del usuario, así como también la del lugar de residencia. Cada uno de estos módulos tienen una alimentación independiente y se interconectan mediante la red WiFi del lugar, siendo ubicados en lugares específicos que pueden ser o no escogidos libremente por el usuario.

El proyecto cuenta con un módulo capaz de detectar fugas de humo y/o gas que puedan ser nocivas para el usuario o que puedan iniciar un incendio. También cuenta con un módulo que detecta la presencia de movimiento no deseado en el hogar cuando se está ausente, presentando la opción de verificación visual mediante fotos tomadas por la(s) cámara(s) del módulo, las cuales se envían directamente al dispositivo móvil del usuario en tiempo real. Así mismo, se cuenta con un módulo adicional capaz de detectar la apertura no deseada de puertas y/o ventanas. Cuando se detecta una anomalía en cualquiera de los sensores que componen los módulos, se alerta al usuario mediante el uso de un parlante o buzzer o mediante mensajes de texto enviados vía Telegram / Whatsapp, dependiendo de la anomalía detectada. El módulo principal se encarga de procesar todos los datos recibidos por los demás sensores, actuando según la naturaleza de los mismos. Adicionalmente, este módulo es capaz de alertar a las autoridades en caso de emergencia mediante una llamada (o SMS) al 123 y/o a una persona de confianza.


## Materiales Requeridos

- Módulo ESP32
- Módulos NodeMCU ESP8266 V2
- ESP32-CAM con cámara OV2640
- Sensor de gas MQ2
- Módulo celular GSM GPRS SIM800L V2.0 con antena
- Sensor de movimiento PIR HC-SR501
- Cerraduras magnéticas Reed Switch
- Parlante o Buzzer


## Composición Básica del Proyecto

### Módulo Principal (Procesamiento):



### Módulo 1 (Detección de Anomalías):


<p align="center">
<img src="https://user-images.githubusercontent.com/82488285/162789558-f67f2c19-4ac0-4547-8c2f-4abfbaa2c337.png" width="600">
</p>


### Módulo 2 (Detección de Movimiento No Deseado):


<p align="center">
<img src="https://user-images.githubusercontent.com/82488285/162789827-dddb0527-bab6-4b47-befe-0c9e52a6fa49.png" width="600">
</p>


### Módulo 3 (Monitoreo Puertas y/o Ventanas):


<p align="center">
<img src="https://user-images.githubusercontent.com/82488285/162789680-ee23d751-6e48-4c2b-8618-8168829db35e.png" width="400">
</p>


## Requerimientos Funcionales



## Requerimientos No Funcionales


## Hardware

.........

### *ESP32*


<p align="center">
<img src="https://user-images.githubusercontent.com/82488285/162795002-6cd33a17-a564-40f8-aed3-581d991ab6c5.png" width="400">
</p>


El ESP32 es usado en el proyecto para procesar todos los datos recibidos por los demás módulos y tomar decisiones con respecto a dichos datos. Sus características son las siguientes:

* Integra un receptor / emisor Bluetooth, con 32 entradas E/S digitales sobre una CPU de 32 bits.
* Procesador Tensilica Xtensa 32bits LX6 de hasta 240 MHz.
* Wi-Fi: 802.11b/g/n/e/i (802.11n @ 2.4 Ghz hasta 150 Mbit/s).
* Bluetooth: v4.2 BR/EDR y bluetooth Low Energy (BLE).
* Rom: 448 KiB.
* SRAM: 520 KiB.
* RTC slow SRAM: 8 KiB.
* RTC fast SRAM: 8 KiB.
* eFuse: 1 Kbit.
* Flash embebida: 0 MiB (ESP32-D0WDQ6, ESP32-D0WD, and ESP32-S0WD chips); 2 MiB (ESP32-D2WD chip); 4 MiB (ESP32-PICO-D4 SIP module).
* Periféricos compatibles: ADC, DAC, I2C, UART, Interfaz CAN 2.0, SPI, I2S, RMII y PWM entre otros.
* Seguridad tipo IEEE 802.11, WFA, WPA/WPA2 y WAPI.
* Encriptación de memoria Flash.
* Criptografía soportada por acelerador de hardware: AES, SHA-2, RSA, ECC, RNG.
* Voltaje de trabajo 3.3 VDC.
* Energía y datos vía conector microUSB 5 VDC.


### *NodeMCU ESP8266 V2*


<p align="center">
<img src="https://user-images.githubusercontent.com/82488285/162795294-3aac7b9c-6aa4-4508-b527-817659e12cfa.png" width="400">
</p>

En el proyecto se utiliza un ESP8266 por cada módulo (a excepción del módulo principal y el módulo 2) para recibir los datos medidos por cada uno de los sensores, realizando un pre-procesamiento de dichos datos según sea el caso. Además, se encargan de entregar los resultados al módulo principal. Las características del ESP8266 son las siguientes:

* Tiene como núcleo un SoM ESP-12E que a su vez está basado en el SoC Wi-Fi ESP8266.
* Integra además el conversor USB-Serial TTL CP2102 y un conector micro-USB necesario para la programación y comunicación a PC.
* Posee un regulador de voltaje de 3.3V en placa, esto permite alimentar la placa directamente del puerto micro-USB o por los pines 5V y GND.
* Los pines de entradas/salidas (GPIO) trabajan a 3.3V por lo que para conexión a sistemas de 5V es necesario utilizar conversores de nivel.
* Viene con un firmware pre-instalado que permite trabajar con el lenguaje interpretado LUA, enviandole comandos mediante el puerto serial (Chip conversor USB-serial CP2102). Además, permite el desarrollo de aplicaciones en diferentes lenguajes como: Arduino, MicroPython, C/C++, Scratch, entre otros.
* El SoC (System On a Chip) ESP8266 integra un potente microcontrolador con arquitectura de 32 bits y conectividad Wi-Fi.
* El SoM (System on Module) ESP-12E integra en un módulo el SoC ESP8266, una memoria FLASH, un cristal oscilador y una antena WiFi en su PCB.
* Voltaje de Alimentación: 5V DC.
* Frecuencia de Reloj: 80 MHz / 160 MHz.
* Instruction RAM: 32 KB.
* Data RAM: 96 KB.
* Memoria Flash Externa: 4 MB.
* Pines Digitales GPIO: 17 (4 pueden configurarse como PWM a 3V3).
* Pin Analógico ADC: 1 (0-1V).
* Puerto Serial UART: 2.
* 802.11 b/g/n.
* Potencia de salida de +19.5 dBm en modo 802.11b.
* Corriente de fuga menor a 10 μA.
* Consumo de potencia Standby < 1.0mW (DTIM3).
* Interface I2S para apliaciones de audio de alta calidad.
* Reguladores de voltaje lineales "low-dropout" en chip.


### *ESP32-CAM*


<p align="center">
<img src="https://user-images.githubusercontent.com/82488285/162795518-86eb8827-2ba9-493d-928a-39a2a98ef25e.png" width="400">
</p>

La ESP32-CAM es utilizada para capturar imágenes de un posible movimiento no deseado para su posterior identificación. Este módulo se encarga de enviarle dichas fotos al módulo principal para dicha identificación. Las características del ESP-CAM son las siguientes:

* Permite hacer streaming de vídeo e imágenes y servirlas a la red creando un servidor local en el mismo chip.
* Aún con toda la carga de procesamiento computacional, el ESP32 aún tiene potencia para hacer otras tareas como reconocimiento facial.
* Entre las principales aplicaciones del ESP32-CAM están las cámaras IP de videovigilancia, los controladores con cámara para transmitir imágenes de un robot móvil, o como sensor para un sistema de visión por computadora básico.
* Es importante mencionar que a mayor resolución tiene menor cantidad de cuadros por segundo transmitidos (FPS).
* Para programar el ESP32-CAM es necesario adicionar un conversor usb-serial externo como el CP2102.
* El módulo ESP32-CAM puede alimentarse con 5V o 3V, se recomienda utilizar una fuente de 5 VDC / 1 A y colocar un capacitor de 100 μF en paralelo con la fuente de alimentación para filtrar los picos de corriente.
* Los pines de entrada / salida (GPIO) trabajan a 3.3 V, por lo que para la conexión a sistemas de 5 V es necesario utilizar conversores de nivel.
* El SoC (System On a Chip) ESP32 es la evolución del ESP8266, diseñado para superar a su antecesor en capacidad de procesamiento y conectividad, integra un potente microcontrolador con arquitectura de 32 bits, conectividad Wi-Fi y Bluetooth.
* El SoM (System on Module) ESP-32S integra en un módulo el SoC ESP32, una memoria FLASH, un cristal oscilador y una antena WiFi en su PCB.
* La plataforma ESP32 permite el desarrollo de aplicaciones en diferentes lenguajes de programación, frameworks, librerías y recursos diversos. Los más comunes a elegir son: Arduino (en lenguaje C++), Esp-idf (Espressif IoT Development Framework) desarrollado por el fabricante del chip, Simba Embedded Programming Platform (en lenguaje Python), RTOS's (como Zephyr Project, Mongoose OS, NuttX RTOS), MicroPython, LUA, Javascript (Espruino, Duktape, Mongoose JS), Basic.
* CPU: Dual core Tensilica Xtensa LX6 (32 bit).
* Wifi 802.11b/g/n, Bluetooth 4.2.
* Antena PCB, también disponible conexión a antena externa.
* 520 KB SRAM interna, 4 MB SRAM externa.
* Soporta UART / SPI / I2C / PWM / ADC / DAC.
* Incluye socket para TF card micro-SD.
* Cámara OV2640.
* Resolución fotos: 1600 x 1200 pixels.
* Resolución vídeo: 1080p30, 720p60 y 640x480p90
* Incluye LED de flash en placa.
* Óptica de 1/4"


### *MQ-2*


<p align="center">
<img src="https://user-images.githubusercontent.com/82488285/162796111-5e2a5bc4-4d76-4016-ad09-993953034b36.png" width="400">
</p>

El sensor MQ2 es utilizado para la detección de altos niveles de humo (representando un incendio) y de altos niveles de gas (posible intoxicación y/o inicio de incendio). Las características de dicho sensor son las siguientes:

* El MQ-2 puede detectar concentraciones humo y gas combustible de 300 a 10000 ppm (partes por millón).
* Tiene una alta sensibilidad (Rin aire / gas típico de Rin ≥ 5) y un tiempo de respuesta rápido (≤ 10 segundos).
* Tiempo de recuperación: ≤ 30 segundos.
* La salida del sensor es una resistencia análoga.
* Para su uso se debe alimentar con 5V, añadir una resistencia de carga y conectar la salida al conversor análogo – digital.
* Incorpora una board que adapta el sensor para su fácil conexión en protoboard o arduinos.
* Cuenta con un amplificador LM393 y un potenciometro para modificar la ganancia del sensor.
* Temperatura de operación: -20 ℃ ~ + 55 ℃.
* Resistencia de calentamiento: 31 ω ± 3 ω.
* Corriente de calefacción: ≤ 180 mA.
* Calentamiento Voltaje: 5.0 V ± 0.2 V.
* Energía de calefacción: ≤ 900 mW.
* Voltaje 10.Measuring: ≤ 24 V.


### *GSM GPRS SIM800L V2.0*


<p align="center">
<img src="https://user-images.githubusercontent.com/82488285/164934247-c4da0bd2-d571-42d6-baca-6dcdc7e2347d.png" width="400">
</p>

El módulo GSM es utilizado para alertar a las autoridades en caso de emergencia mediante una llamada (o SMS) al 123 y/o a una persona de confianza. Las características de este módulo son las siguientes:

* Este módulo trabaja con tarjetas de telefonía celular, por lo que cuentan con un código IMEI para su registro, pero debido a inconvenientes de fabricación en el mercado chino, están llegando con un IMEI diferente al descrito en la etiqueta. Por consiguiente se sugiere que al momento de instalar la Sim Card de telefonía celular, llamar a atención al cliente del operador elegido y por medio de un asesor solicitar el registro del IMEI original del módulo (obtenido por comandos AT) junto con el número de la Sim Card a usarse, para así evitar futuros bloqueos del módulo.
* Es un dispositivo quad-band GSM/GPRS, trabaja en las frecuencias GSM850MHz, EGSM900MHz, DCS1800MHz y PCS1900MHz.
* Permite añadir voz, texto, datos y SMS en un pequeño paquete. Esta versión cuenta con un conector uFL.
* Se requiere un microcontrolador que permita la comunicación UART para controlar el módulo.
* Voltaje de Operación: 3.4 V ~ 4.4 V DC.
* Nivel Lógico de 3 V a 5 V.
* Consumo de corriente (max): 500 mA.
* Consumo de corriente (sleep): 0.7 mA.
* Interfaz: Serial UART.
* Quad-band 850/900/1800/1900MHz – se conectan a cualquier red mundial GSM con cualquier SIM 2G
* Trabaja solo con tecnología 2G.
* Envía y recibe mensajes SMS.
* Envía y recibe datos GPRS (TCP/IP, HTTP, etc).
* Tiene un receptor FM.
* Es controlado por Comandos AT (3GPP TS 27.007, 27.005 y SIMCOM enhanced AT Commands).
* Interfaz de comandos AT con detección “automática” de velocidad de transmisión.
* Soporta A-GPS.
* Datos GPRS: Velocidad máxima de transmisión 85.6 Kbps, Protocolo TCP/IP en chip, Codificacion: CS-1, CS-2, CS-3 y CS-4, Soporta USSD.
* Soporta Reloj en tiempo real (RTC).
* Velocidades de transmisión serial desde 1200bps hasta 115200bps.
* Tamaño de la SIM: Micro SIM.

### *PIR HC-SR501*


<p align="center">
<img src="https://user-images.githubusercontent.com/82488285/162796623-381d873d-df4d-441e-aa71-d5b5983336b8.png" width="400">
</p>

El sensor PIR es utilizado para detectar un posible movimiento no deseado para su posterior identificación. Las características de este sensor son las siguientes:

* Tiene 3 pines de conexión +5V, OUT (3.3V) y GND, y dos resistencias variables de calibración (Ch1 y RL2).
* Con la resistencia Ch1 se establece el tiempo que se va a mantener activa la salida del sensor. Una de las principales limitaciones de este módulo es que el tiempo mínimo que se puede establecer es de más o menos 3 segundos. Si se cambia la resistencia por otra de 100 kΩ, se puede bajar el tiempo mínimo a más o menos 0,5 segundos.
* Con la resistencia RL2 se puede establecer la distancia de detección, la cual puede variar entre 3 y 7 metros.
* La posibilidad de mantener activa la salida del módulo durante un tiempo determinado permite usarlo directamente para prácticamente cualquier aplicación sin necesidad de usar un microcontrolador.
* Contiene un sensor piroeléctrico (Pasivo) infrarrojo (También llamado PIR).
* El módulo incluye el sensor, un lente, el controlador PIR BISS0001, un regulador y todos los componentes de apoyo para una fácil utilización.
* Lente fresnel de 19 zonas, ángulo < 100°.
* Salida activa alta a 3.3 V.
* Redisparo configurable mediante jumper de soldadura.
* Consumo de corriente en reposo: < 50 μA.
* Voltaje de alimentación: 4.5 VDC a 20 VDC.



### *Reed Switch*


<p align="center">
<img src="https://user-images.githubusercontent.com/82488285/162848011-a10ca745-b823-44db-a6c8-3cef3b46d7ae.png" width="400">
</p>

El sensor magnético se utiliza para detectar la apertura no deseada de puertas y/o ventanas en el hogar. Este sensor presenta las siguientes características:

* Contact Configuration:	SP-NO.
* Maximum Switching Current:	100 mA.
* Maximum Switching Power:	1 VA.
* Maximum Switching Voltage:	24 V ac/dc.
* Contact Resistance:	150 mΩ.
* Contact Material:	Rhodium
* Maximum Release Time: 0.05 ms
* Operating Time Including Bounce:	0.6 ms


### *Parlante / Buzzer*


<p align="center">
<img src="https://user-images.githubusercontent.com/82488285/162848525-99e7818a-45b0-4700-bc31-e431889eb0e5.png" width="300">
</p>

El parlante o buzzer es utilizado para alertar al usuario de una posible emergencia, como lo es un incendio o una fuga de gas. Este parlante / buzzer tiene las siguientes características:

* Voltaje: 4 a 8 VDC.
* Corriente máxima: 30 mA / 5 VDC.
* Frecuencia Resonante: 2500 ± 300 HZ.
* Presión más suave => 85 db / 10 cm.
* Temperatura de funcionamiento: -20 a 70 grados.


## Software




## Modelado en PCB e Impresión 3D




