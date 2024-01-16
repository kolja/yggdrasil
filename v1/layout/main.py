import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.holdtap import HoldTap
from keymap import Keymap

print("Starting (right)")

keyboard = KMKKeyboard()
holdtap = HoldTap()

# unused for now:
SZ_CAP = simple_key_sequence( ( KC.RSFT(KC.S), KC.RSFT(KC.S),))

class localDefinitions:
    def __init__(self):
        self.TABRIGHT = KC.TAB
        self.TABLEFT = KC.LSFT(KC.TAB)
        self.SZ = KC.LALT(KC.S)
        # tap => ¨, hold => KC.LALT
        self.LALT = KC.HT(KC.LALT(KC.U), KC.LALT)
        # tap => s, hold => LGUI
        self.CMD_S = KC.HT(KC.S, KC.LGUI, prefer_hold=False)
        self.CMD_E = KC.HT(KC.E, KC.LGUI, prefer_hold=False)
        self.PERCENT = KC.HT(KC.PERCENT, KC.LGUI)
        # Layers
        self.NUM = 1
        self.NAV = 2

LOC = localDefinitions()

split = Split(
    split_type=SplitType.UART,
    split_side=SplitSide.RIGHT,
    use_pio=True,
    split_target_left=False,
    data_pin=board.GP0,
    data_pin2=board.GP1)

layers = Layers({(1,2):3})

keyboard.modules.append(split)
keyboard.modules.append(layers)
keyboard.modules.append(holdtap)

keyboard.col_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11)
keyboard.row_pins = (board.GP22, board.GP21, board.GP17, board.GP16)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = Keymap(KC, LOC).keymap
# keyboard.keymap = [
#     [ # MAIN LAYER
#         KC.Q, KC.W, KC.F, KC.P, KC.B,      		        KC.J, KC.L, KC.U, KC.Y, KC.BSPACE,
#         KC.A, KC.R, CMD_S, KC.T, KC.G,      		        KC.M, KC.N, CMD_E, KC.I, KC.O,
#         KC.Z, KC.X, KC.C, KC.D, KC.V,      		        KC.K, KC.H, KC.COMM, KC.DOT, KC.SLASH,
#         KC.NO, KC.LCTRL, LALT, KC.MO(NAV), KC.LCMD, KC.ESCAPE, KC.MO(NUM), KC.RSFT, KC.SPACE, KC.NO,
#     ],
#     [ # NUM LAYER
#         KC.QUES, KC.EXLM, KC.AT, KC.HASH, KC.QUOTE,     KC.N0, KC.N1, KC.N2, KC.N3, KC.EQUAL,
#         KC.TILDE, KC.DOLLAR, PERCENT, KC.CIRC, KC.DQT, KC.PLUS, KC.N4, KC.N5, KC.N6, KC.ASTERISK,
#         KC.GRAVE, KC.AMPR, KC.COLON, KC.SCOLON, KC.UNDERSCORE, KC.MINUS, KC.N7, KC.N8, KC.N9, KC.SLASH,
#         KC.NO, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 	    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,
#     ],
#     [ # NAV LAYER
#         KC.RELOAD, KC.N1, KC.LBRC, KC.RBRC, KC.BSLASH,	KC.NO, KC.LCBR, KC.RCBR, KC.COLON, KC.SCOLON,
#         KC.NO, KC.NO, KC.LEFT_PAREN, KC.RIGHT_PAREN, KC.SLASH, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.ENTER,
#         KC.NO, KC.NO, KC.LABK, KC.RABK, KC.PIPE,		KC.NO, KC.ESCAPE, KC.TAB, KC.N9, KC.X,
#         KC.NO, KC.NO, KC.NO, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TAB, KC.LALT(KC.TAB), KC.NO,
#     ],
#     [ # F KEY LAYER
#         KC.F1, KC.F2, KC.F3, KC.F4, KC.F5,      		KC.F6, KC.F7, KC.F8, KC.F9, KC.F10,
#         KC.HYPR(KC.A), KC.R, SZ, KC.LCMD(KC.SPACE), KC.G, KC.LCTRL(KC.H), KC.LCTRL(KC.J), KC.LCTRL(KC.K), KC.LCTRL(KC.L), KC.LCTRL(KC.ENTER),
#         KC.Z, KC.X, KC.C, KC.D, KC.V,      		        KC.K, KC.H, KC.COMM, KC.DOT, KC.ENTER,
#         KC.NO, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 	    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,
#     ],
# ]

if __name__ == "__main__":
    keyboard.go()

