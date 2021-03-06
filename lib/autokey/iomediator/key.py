# Key codes enumeration
import enum


@enum.unique
class Key(str, enum.Enum):

    LEFT = "<left>"
    RIGHT = "<right>"
    UP = "<up>"
    DOWN = "<down>"
    BACKSPACE = "<backspace>"
    TAB = "<tab>"
    ENTER = "<enter>"
    SCROLL_LOCK = "<scroll_lock>"
    PRINT_SCREEN = "<print_screen>"
    PAUSE = "<pause>"
    MENU = "<menu>"
    
    # Modifier keys
    CONTROL = "<ctrl>"
    ALT = "<alt>"
    ALT_GR = "<alt_gr>"
    SHIFT = "<shift>"
    SUPER = "<super>"
    HYPER = "<hyper>"
    CAPSLOCK = "<capslock>"
    NUMLOCK = "<numlock>"
    META = "<meta>"
    
    F1 = "<f1>"
    F2 = "<f2>"
    F3 = "<f3>"
    F4 = "<f4>"
    F5 = "<f5>"
    F6 = "<f6>"
    F7 = "<f7>"
    F8 = "<f8>"
    F9 = "<f9>"
    F10 = "<f10>"
    F11 = "<f11>"
    F12 = "<f12>"
    F13 = "<f13>"
    F14 = "<f14>"
    F15 = "<f15>"
    F16 = "<f16>"
    F17 = "<f17>"
    F18 = "<f18>"
    F19 = "<f19>"
    F20 = "<f20>"
    F21 = "<f21>"
    F22 = "<f22>"
    F23 = "<f23>"
    F24 = "<f24>"
    F25 = "<f25>"
    F26 = "<f26>"
    F27 = "<f27>"
    F28 = "<f28>"
    F29 = "<f29>"
    F30 = "<f30>"
    F31 = "<f31>"
    F32 = "<f32>"
    F33 = "<f33>"
    F34 = "<f34>"
    F35 = "<f35>"
    
    # Other
    ESCAPE = "<escape>"
    INSERT = "<insert>"
    DELETE = "<delete>"
    HOME = "<home>"
    END = "<end>"
    PAGE_UP = "<page_up>"
    PAGE_DOWN = "<page_down>"

    # Numpad
    NP_INSERT = "<np_insert>"
    NP_DELETE = "<np_delete>"
    NP_HOME = "<np_home>"
    NP_END = "<np_end>"
    NP_PAGE_UP = "<np_page_up>"
    NP_PAGE_DOWN = "<np_page_down>"
    NP_LEFT = "<np_left>"
    NP_RIGHT = "<np_right>"
    NP_UP = "<np_up>"
    NP_DOWN = "<np_down>"
    NP_DIVIDE = "<np_divide>"
    NP_MULTIPLY = "<np_multiply>"
    NP_ADD = "<np_add>"
    NP_SUBTRACT = "<np_subtract>"
    NP_5 = "<np_5>"

    @classmethod
    def is_key(cls, key_string: str) -> bool:
        """
        Returns if a string represents a key.
        """
        # Key strings must be treated as case insensitive - always convert to lowercase
        # before doing any comparisons
        lowered_key_string = key_string.lower()
        try:
            cls(lowered_key_string)
        except ValueError:
            return lowered_key_string.startswith("<code")
        else:
            return True


NAVIGATION_KEYS = [Key.LEFT, Key.RIGHT, Key.UP, Key.DOWN, Key.BACKSPACE, Key.HOME, Key.END, Key.PAGE_UP, Key.PAGE_DOWN]
