class Keymap:
    def __init__(self, KC, LOC):
        self.keymap = [
        [ # MAIN LAYER
            KC.Q, KC.W, KC.F, KC.P, KC.B,      		        KC.J, KC.L, KC.U, KC.Y, KC.BSPACE,
            KC.A, KC.R, LOC.CMD_S, KC.T, KC.G,              KC.M, KC.N, LOC.CMD_E, KC.I, KC.O,
            KC.Z, KC.X, KC.C, KC.D, KC.V,      		        KC.K, KC.H, KC.COMM, KC.DOT, KC.SLASH,
            KC.NO, KC.LCTRL, LOC.LALT, KC.MO(LOC.NAV), KC.LCMD, KC.ESCAPE, KC.MO(LOC.NUM), KC.RSFT, LOC.CMD_SPACE, KC.NO,
        ],
        [ # NUM LAYER
            KC.QUES, KC.EXLM, KC.AT, KC.HASH, KC.QUOTE,             KC.PLUS,  KC.N7, KC.N8, KC.N9, KC.EQUAL,
            KC.TILDE, KC.DOLLAR, LOC.PERCENT, KC.CIRC, KC.DQT,      KC.MINUS, KC.N4, KC.N5, KC.N6, KC.ASTERISK,
            KC.GRAVE, KC.AMPR, KC.COLON, KC.SCOLON, KC.UNDERSCORE,  KC.N0,    KC.N1, KC.N2, KC.N3, KC.SLASH,
            KC.NO, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 	            KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,
        ],
        [ # NAV LAYER
            KC.RELOAD, KC.NO, KC.LBRC, KC.RBRC, KC.BSLASH,	KC.NO, KC.LCBR, KC.RCBR, LOC.TABLEFT, LOC.TABRIGHT,
            KC.NO, KC.NO, KC.LEFT_PAREN, KC.RIGHT_PAREN, KC.SLASH, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.ENTER,
            KC.TAB, KC.NO, KC.LABK, KC.RABK, KC.PIPE,		KC.NO, KC.ESCAPE, KC.TAB, KC.N9, KC.X,
            KC.NO, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,      KC.TRNS, KC.TRNS, KC.LGUI, KC.LALT(KC.TAB), KC.NO,
        ],
        [ # F KEY LAYER
            KC.F1, KC.F2, KC.F3, KC.F4, KC.F5,      		KC.F6, KC.F7, KC.F8, KC.F9, KC.F10,
            KC.HYPR(KC.A), KC.HYPR(KC.R), KC.HYPR(KC.S), KC.HYPR(KC.T), KC.HYPR(KC.G), KC.LGUI(KC.LEFT), KC.LGUI(KC.DOWN), KC.LGUI(KC.UP), KC.LGUI(KC.RIGHT), KC.ENTER,
            KC.Z, KC.X, KC.C, KC.D, KC.V,      		        KC.LCTL(KC.LEFT), KC.LCTL(KC.DOWN), KC.LCTL(KC.UP), KC.LCTL(KC.RIGHT), KC.LCTL(KC.ENTER),
            KC.NO, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 	    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,
        ],
    ]
