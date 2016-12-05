# -*- coding: utf-8 -*-
import argparse
import os

parser = argparse.ArgumentParser(description='argparse tester')

parser.add_argument("-v", "--verbose",
                    help="increase output verbosity", action="store_true")
parser.add_argument(
    "-f", "--file", help="which file to be check", default="data.csv")

args = parser.parse_args()

if args.verbose:
    print("Hello world!")

if args.file:
    if os.path.exists(args.file):
        print("File %s is exist!" % args.file)
    else:
        print("File %s is NOT exist!" % args.file)
