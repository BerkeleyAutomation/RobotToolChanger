import time
#import Adafruit-GPIO.SPI as SPI
import Adafruit_MCP3008
import socket

CLK = 4
MISO = 17
MOSI = 27
CS = 22

mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    value = mcp.read_adc(0) # true value
    client_socket.sendto(str(value), ("127.0.0.1", 8008))
    #print(value)
    time.sleep(0.5)
