import serial
import time
import serial.tools.list_ports as port_list
from pathlib import Path
from datetime import datetime

# Path("/sensor_logs/").mkdir(parents=True, exist_ok=True)

ports_init = list(port_list.comports())
print("Please connect the device...")
while True:
    time.sleep(1)
    ports_ = list(port_list.comports())
    new_dev = list(set(ports_) - set(ports_init))
    if len(new_dev):
        break

print(f"Device found on ", new_dev[0].name)

ser = serial.Serial(new_dev[0].name, 9600)
FLAG1 = True
file_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
while True:
    s = ser.readline()
    with open(f'senLog_{file_name}.txt', 'ab') as fb:
        fb.write(s)
    if FLAG1:
        print('Data is capturing....')
        FLAG1 = False
    # print(s)
