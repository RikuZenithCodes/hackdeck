import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.pixel import Pixel
from kmk.modules.oled import Oled, OledDisplayMode
from kmk.modules.macros import Macros, Press, Release, Tap

keyboard = KMKKeyboard()


KEY_PINS = [board.D3, board.D4, board.D2, board.D1, board.D0]  

keyboard.matrix = KeysScanner(
    pins=KEY_PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
        KC.MACRO("Hello world!"),
        KC.Macro(Press(KC.LGUI), Tap(KC.S), Release(KC.LGUI)),
    ]
]

macros = Macros()
keyboard.modules.append(macros)


pixel = Pixel(pin=board.D6, num_pixels=1, rgb_order=(1, 0, 2))  
keyboard.modules.append(pixel)
pixel.set_brightness(0.2)
pixel.set_pixel(0, (255, 0, 0))  

encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = ((board.D9, board.D8, board.D7),)  
encoder.map = ((KC.VOLD, KC.VOLU, KC.MUTE),)     

oled = Oled(
    i2c=board.I2C(),
    address=0x3C,               
    display_mode=OledDisplayMode.TXT,
    flip=False,
    invert=False
)
keyboard.modules.append(oled)

oled.set_lines("MacroPad", "by KMK", "", "")

# ----- Go -----
if __name__ == '__main__':
    keyboard.go()