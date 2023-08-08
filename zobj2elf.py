#!/usr/bin/env python
from argparse import ArgumentParser, Namespace

from makeelf.elf import ELF
from makeelf.elfstruct import ET

from obj import ZObj


def main(args: Namespace) -> int:
    obj = ZObj(open(args.input, "rb"))
    elf = ELF(e_type=ET.ET_REL)  # makeelf does not support Z80 machine type

    if args.output is None:
        args.output = args.input[:args.input.rfind(".")] + ".elf"
    
    with open(args.output, "wb") as f:
        f.write(bytes(elf))

    return 0


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="zobj2elf", description="Convert Z80ASM object files to ELF"
    )

    parser.add_argument("input", help="Input file")
    parser.add_argument("-o", "--output", help="Output file")

    exit(main(parser.parse_args()))
