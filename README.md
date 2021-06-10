# Smart toothbrush

![](https://github.com/soheil-star01/toothbrush_prj/blob/main/images/toothbrush%20(1).jpg)

![](https://github.com/soheil-star01/toothbrush_prj/blob/main/images/toothbrush%20(2).jpg)

### Software installation
To get data from the toothbrush you first need to have installed Python 3.X.X (64bit). 
You can download the official setup file from [here.](https://www.python.org/downloads/)

Then you need install the `requirements`. you can do it by simply running below command in the command line while your 
inside the `toothbrush_prj` directory: 
```shell
pip install -r requirements
```
After successfully installing the requirements, you can simply run the Python file using:
```shell
python main.py
```
Then on the command line you would get this message which shows the app is running.
```shell
Please connect the device...
```
####Note:
>If you have Python 2 on your computer as well, you need to use `python3` instead of `python` and `pip3` instead of `pip`.
---
### Connecting the toothbrush
1- disconnect the device if you have already connected it to USB port.

2- run the python app and wait till you get this message: `Please connect the device...`

3- connect the toothbrush and now you should get this message: `Data is capturing....`

4- to stop the program press `ctrl + c` or close the command prompt

5- the captured data is stored in text file(s) which the name starts with `senLog`