#!/usr/bin/env python
from argparse import ArgumentParser, Namespace
from io import BufferedReader


class ZObj:
    """Represents a Z80ASM object file"""

    def __init__(self, file: BufferedReader):
        self.signature = file.read(8).decode("ascii")
        if self.signature.startswith("Z80") == False or self.signature[4:6] != "MF":
            # Bad signature
            raise Exception("Bad signature: %s" % self.signature)

        if not self.version in [17]:
            raise Exception("Unsupported version: %d" % self.version)

        module_name_offset = int.from_bytes(file.read(4), "little")
        expressions_offset = int.from_bytes(file.read(4), "little")
        module_names_offset = int.from_bytes(file.read(4), "little")
        external_names_offset = int.from_bytes(file.read(4), "little")
        machine_code_offset = int.from_bytes(file.read(4), "little")

        if self.version >= 18:
            self.cpu_id = int.from_bytes(file.read(4), "little")
            self.swap_ix_iy = int.from_bytes(file.read(4), "little")

    @property
    def version(self) -> int:
        return int(self.signature[6:8])


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
