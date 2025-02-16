STYLES = {
    "bold"             : 1,
    "italic"           : 3,
    "underline"        : 4,
    "strikethrough"    : 9,
    "gray"             : 30,
    "red"              : 31,
    "green"            : 32,
    "yellow"           : 33,
    "blue"             : 34,
    "magenta"          : 35,
    "cyan"             : 36,
    "white"            : 37,
    "inverted-gray"    : 40,
    "inverted-red"     : 41,
    "inverted-green"   : 42,
    "inverted-yellow"  : 43,
    "inverted-blue"    : 44,
    "inverted-magenta" : 45,
    "inverted-cyan"    : 46,
    "inverted-white"   : 47,
}

logo = r'''   _____ _ _   ____                _      
  / ____(_) | |  _ \ _    _ /SSSS | |     
 | |    | | |_| |_) | |  | |     s| |___  
 | |   _| | __|  __/| |  | |\SSS\ |  __ \ 
 | |__| | | |_| |   | |__| |s    || |  | |
  \_____| |\__|_|    \____/  SSSS/|_|  |_|'''

def stylise(msg:str, style: str):
    """add style / color to your string

    Args:
        msg (str): string to be stylised
        style (str): style | options -> [`bold`, `italic`, `underline`, `strikethrough`, `gray`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `inverted-gray`, `inverted-red`, `inverted-green`, `inverted-yellow`, `inverted-blue`, `inverted-magenta`, `inverted-cyan`, `inverted-white`]

    Returns:
        str: stylised string
    """
    return f"\033[{STYLES[style]}m" + msg + "\033[0m"
