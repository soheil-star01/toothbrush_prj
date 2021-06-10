import serial
import time
import sys
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

os_name = sys.platform
os_valid = True
if os_name == 'darwin':
    print('Mac OS')
    ser = serial.Serial('/dev/' + new_dev[0].name, 115200)
elif 'win' in os_name:
    print('Windows OS')
    ser = serial.Serial(new_dev[0].name, 115200)
else:
    os_valid = False
    print('OS is not supported!!')

FLAG1 = True
file_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
while os_valid:
    s = ser.readline()
    with open(f'senLog_{file_name}.txt', 'ab') as fb:
        fb.write(s)
    if FLAG1:
        print('Data is capturing....\nPress Ctrl+C to exit')
        FLAG1 = False
    # print(s)