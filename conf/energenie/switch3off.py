from gpiozero import Energenie
import requests
switchsocket = 3
Energenie(switchsocket, initial_value=False)
