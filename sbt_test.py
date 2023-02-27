import serial

i = 0
b = i.to_bytes(1,'little')
SerialPortObj = serial.Serial('/dev/ttyUSB0')
SerialPortObj.write(bytes(b))

print('\nStatus -> ',SerialPortObj) 
 
SerialPortObj.close()    
