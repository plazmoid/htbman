#!/usr/bin/env python3
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
import subprocess
import sys

# TODO
# argparser
# setup.py to access from any dir
# which instruments are used/learned
# get the name and IP of the box from HTB
# when the box is rooted, move all in db, gather all info (flags, utilities, compressed files)
# some kind of api?

class HTBox: pass ####################

def init_scan(ip):
    pass
# subprocess nmaps 

def new_box(name):
    bwd = Path('boxes') 
    bwd /= name # box working directory
    bwd.mkdir()
    with open(bwd / 'walkthrough.txt', 'w') as fo:
        cur_time = datetime.now().strftime("%d-%m-%Y %H:%M")
        fo.write(f'# Started {name} at {cur_time}')


def main():
    parser = ArgumentParser()
    parser.add_argument('-n', '--new', dest='name', help="Create new box's folder with walkthrough.txt")
    parser.add_argument('-i', '--init-scan', dest='ip', 
            help="Perform initial scan (nmap -A -p$(nmap -p-) ...) IP")
    parser.add_argument('-f', '--finish', dest='fin', help="Finish the box")
    args = parser.parse_args(sys.argv[1:])
    if args.name:
        new_box(args.name)
    if args.ip:
        init_scan(args.ip)

    if len(sys.argv) == 1:
        parser.print_help()


if __name__ == '__main__':
    main()
