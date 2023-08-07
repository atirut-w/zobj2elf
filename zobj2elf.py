#!/usr/bin/env python
from argparse import ArgumentParser, Namespace


def main(args: Namespace) -> int:
    print("Stub")
    return 0


if __name__ == "__main__":
    parser = ArgumentParser(prog="zobj2elf", description="Convert Z80ASM object files to ELF")

    parser.add_argument("input", help="Input file")
    parser.add_argument("output", help="Output file")

    exit(main(parser.parse_args()))
