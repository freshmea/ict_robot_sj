import serial
import time



def main():
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=3)
    while True:
        try:
            for data in ser.read():
                line = chr(data)
                print(line, end='')
        except:
            pass

if __name__ == '__main__':
    main()