#!/usr/bin/env python3
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
from termcolor import colored
import subprocess
import sys

# TODO
# setup.py to access from any dir
# which instruments are used/learned
# get the name and IP of the box from HTB
# when the box is rooted, move all in db, gather all info (flags, utilities, compressed files)
# some kind of api?

class tty_format:
    QUESTION = colored('[?]', 'yellow')
    INFO = colored('[~]', 'blue')
    WARNING = colored('[!]', 'magenta')
    ERROR = colored('[X]', 'red')


def info(text: str) -> None:
    print(f"{tty_format.INFO} {text}")

def ask(que: str, answers: tuple = ('y', 'n')) -> str:
    while True:
        print(f"{tty_format.QUESTION} {que} [{'/'.join(answers)}]")
        answer = str(input())
        if answer in answers:
            return answer
        
class HTBox:

    def __init__(self, path: str, *args):
        self.vars = self.parse_vars(args)
        self.bwd = Path(path)
        self.name = self.bwd.parts[-1]
        if not self.bwd.exists():
            if ask('Path does not exist. Create?') == 'y':
                self.new_box()
        
    def init_scan(self):
        pass
    # subprocess nmaps 

    def parse_vars(self, vars: tuple) -> dict:
        result = {}
        for var in vars:
            if '=' in var:
                k, v = var.split('=')
                result[k.strip()] = v.strip()
        return result

    def new_box(self): 
        self.bwd.mkdir()
        with open(self.bwd / 'walkthrough.txt', 'w') as fo:
            cur_time = datetime.now().strftime("%d-%m-%Y %H:%M")
            fo.write(f'# Started {self.name} at {cur_time}')


def main():
    sargs = sys.argv
    parser = ArgumentParser()
    #parser.add_argument('-n', '--new', dest='name', help="Create new box's folder with walkthrough.txt")
    parser.add_argument('-i', '--init-scan', dest='ip', 
            help="Perform initial scan (nmap -A -p$(nmap -p-) ...) IP")
    parser.add_argument('-f', '--finish', dest='fin', help="Finish the box")
    parser.add_argument('path', help='Path to folder with box')
    parser.add_argument('vars', help='Box variables: var1=qwe var2=rty', nargs='*')
    args = parser.parse_args(sargs[1:])
    box = HTBox(args.path, args.vars)

    if len(sargs) == 1:
        parser.print_help()


if __name__ == '__main__':
    main()
