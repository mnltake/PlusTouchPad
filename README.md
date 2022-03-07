"# PlusTouchPad" 

![スクリーンショット 2022-03-06 111727](https://user-images.githubusercontent.com/45388626/157047978-bb62a1e4-2f08-49e3-9c31-6142030bc589.png)

![IMG_20220306_182917](https://user-images.githubusercontent.com/45388626/157048201-65a4ba03-f54a-48ea-94f8-3971f283d127.jpg)


# 使用部品

ユニバーサル抵抗膜タッチスクリーンコントローラ AR1010-I/SO

https://eleshop.jp/shop/g/gAA1411/

http://ww1.microchip.com/downloads/en/DeviceDoc/41393A.pdf

タッチスクリーン Intelligent Display Solutions 2.7インチ 4-wire Resistive

https://www.monotaro.com/g/04415528/

1.0/4P★FFCコネクタwith基板 

https://www.aitendo.com/product/11789

SOP/SSOP 20Pin変換基板

https://eleshop.jp/shop/g/gF2R417/

C 10uF * 1 0.1uF * 1 0.01uF * 2

R 20KOhm * 1 4.7KOhm * 1

LED * 1

# library

```pip3 install pynput```

https://github.com/moses-palmer/pynput

# 配線


|(AR1010)| - |(raspberri pi)|
|:-----------:|:------------:|:------------:|
|VDD| - |3.3V|
|VSS| - |GND|
|TX| - |GPIO15(RX)|
|RX| - |GPIO14(TX)|


|(AR1010)| - |(touchpanel)|
|:-----------:|:------------:|:------------:|
||X+||
||X-||
||Y+||
||Y-||
