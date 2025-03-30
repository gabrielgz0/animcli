class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    LIGHT_BLUE = '\033[94m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_RED = '\033[91m'
    LIGHT_CYAN = '\033[96m'
    LIGHT_MAGENTA = '\033[95m'

    @staticmethod
    def colorize(text: str, color: str):
        return f"{color}{text}{BColors.ENDC}"

def get_color(color_name: str):
    color_map = {
        'header': BColors.HEADER,
        'blue': BColors.OKBLUE,
        'green': BColors.OKGREEN,
        'warning': BColors.WARNING,
        'fail': BColors.FAIL,
        'light_blue': BColors.LIGHT_BLUE,
        'light_green': BColors.LIGHT_GREEN,
        'light_yellow': BColors.LIGHT_YELLOW,
        'light_red': BColors.LIGHT_RED,
        'light_cyan': BColors.LIGHT_CYAN,
        'light_magenta': BColors.LIGHT_MAGENTA,
    }

    return color_map.get(color_name.lower(), BColors.FAIL)
