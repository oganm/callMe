import RPi.GPIO as GPIO
import configparser


config = configparser.ConfigParser()
config.read('.config')
buttonIn = int(config['piConfig']['buttonIn'])
email = int(config['piConfig']['buttonIn'])

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonIn,GPIO.IN)



