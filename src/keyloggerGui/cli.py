import argparse
from keylogger import KeyLogger

def main():
    parser = argparse.ArgumentParser(description="Run a Keylogger Gui For S n' Gs, press shift+ctrl+x to quit")
    parser.add_argument('-f',
                        '--font',
                        type=str,
                        default="Helvetica",
                        help="The font name, e.g. Helvetica")
    parser.add_argument('-s',
                        '--size',
                        type=int,
                        default=99,
                        help="The size of the font in pixels")
    parser.add_argument('-w',
                        '--weight',
                        type=str,
                        choices=["bold", "boldface", "normal"],
                        default="normal",
                        help="Font weight: bold, boldface, normal")
    parser.add_argument('-t',
                        '--text-color',
                        type=str,
                        default="#ff00ff",
                        help="Text Color as text, e.g. red, black, purple, color codes also work")
    parser.add_argument('-b',
                        '--background-color',
                        type=str,
                        default="#6600CC",
                        help="Color of the Background in text")
    args = parser.parse_args()
    k = Keylogger(args.font,
                  args.size,
                  args.weight,
                  args.text_color,
                  args.background_color
    )
    k.run()
