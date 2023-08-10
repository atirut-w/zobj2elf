#!/usr/bin/env python
from argparse import ArgumentParser, Namespace

from obj import ZObj
from elf import ELF, ISA, Type


def main(args: Namespace) -> int:
    obj = ZObj(open(args.input, "rb"))
    elf = ELF(ISA.Z80, Type.REL) # We don't know if it's executable or not (yet)

    if args.output == None:
        args.output = args.input[:args.input.rfind(".")] + ".elf"
    
    with open(args.output, "wb") as f:
        elf.write(f)

    return 0


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="zobj2elf", description="Convert Z80ASM object files to ELF"
    )

    parser.add_argument("input", help="Input file")
    parser.add_argument("-o", "--output", help="Output file")

    exit(main(parser.parse_args()))
