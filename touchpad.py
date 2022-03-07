#!/usr/bin/python3

import serial,struct,time
from pynput.mouse import Button, Controller
from pynput import keyboard
delta = 1
abs_x=0
abs_y=0
pre_x=0
pre_y=0
move_x=0
move_y=0
pencnt=0
mouse= Controller()
key =keyboard.Controller()

def mapping(x,in_min,in_max,out_min,out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

ser = serial.Serial('/dev/ttyAMA0', baudrate=9600, parity=serial.PARITY_NONE)
while ser.readable():
    (curr_x, curr_y) =mouse.position
    print(f"current={curr_x}:{curr_y}")
    pen_byte = struct.unpack('B',ser.read(1))
    pen =pen_byte[0]& 0b00000001
    if pen_byte[0] >> 7: #1bit目が1なら先頭byte
        recv_data= ser.read(4)
        i_data= struct.unpack('4B',recv_data)
        abs_x = int((recv_data[1]<<5) | (recv_data[0]>>2)) #10bit(X11~X2)
        abs_y = int((recv_data[3]<<5) | (recv_data[2]>>2)) #10bit(Y11~Y2)
        print(f"pen={pen} pencnt={pencnt} x={abs_x} y={abs_y}")
        abs_x =mapping(abs_x,95,930,0,304) #キャリブレーション　横30.4mm*10 に変換　
        abs_y =mapping(abs_y,70,957,0,624) #縦62.4mm*10　に変換　
        if pencnt > 50 and 300 < abs_x and 480 < abs_y :
            mouse.scroll(0,1)
            pencnt = 0
            print("scroll up")
        if pencnt > 50 and 300 < abs_x and 280 < abs_y < 480:
            mouse.scroll(0,-1)
            pencnt = 0
            print("scroll down")
        if pencnt > 50 and abs_x < 50 and 500 < abs_y:
            with key.pressed(keyboard.Key.ctrl):
                key.press('+')
                key.release('+')
            pencnt = 0
            print("ctrl+")
        if pencnt > 50 and abs_x < 50 and 280 < abs_y < 480:
            with key.pressed(keyboard.Key.ctrl):
                key.press('-')
                key.release('-')
            pencnt = 0
            print("ctrl-")
        if abs_y > 280:
            move_x = abs_x - pre_x
            move_y = abs_y - pre_y
            print(f"move={move_x}:{move_y}")
            pre_x = abs_x
            pre_y = abs_y
            if pencnt > 100:
                mouse.press(Button.left)
        elif abs_x < 170 and pen :
            mouse.press(Button.left)
            print("left Click")
        elif abs_x > 170 and pen:
            mouse.press(Button.right)
            print("right Click")

    else:
        move_x = 0
        move_y = 0
    if pen:
        pencnt += 1
    else:
        pencnt=0
        mouse.release(Button.left)
        mouse.release(Button.right)

    if ((move_x!=0 ) or(move_y!=0))and pen:
        mouse.move(delta * move_x ,-delta * move_y)
ser.close()