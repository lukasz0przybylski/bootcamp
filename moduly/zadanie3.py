import sys
import argparse


try:
    f_fname = sys.argv[1]
except IndexError:
    print("nie dales nazwy pliku")
    exit()

parser - argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input file", action="store")
parser.add_argument("-o", "--output", help="output file", action="store")

args = parser.parser_arg()

cleaned_emails = set ()

with open(args.input) as f:
    for line in f:
        line = line.strip().lower()
        f.