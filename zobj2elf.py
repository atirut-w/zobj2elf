#!/usr/bin/env python
from argparse import ArgumentParser, Namespace

from obj import ZObj


def main(args: Namespace) -> int:
    obj = ZObj(open(args.input, "rb"))
    return 0


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="zobj2elf", description="Convert Z80ASM object files to ELF"
    )

    parser.add_argument("input", help="Input file")
    parser.add_argument("-o", "--output", help="Output file")

    exit(main(parser.parse_args()))
