from enum import Enum


class Bitness(Enum):
    BIT32 = 0x01
    BIT64 = 0x02


class Endianness(Enum):
    LITTLE = 0x01
    BIG = 0x02


class ABI(Enum):
    LINUX = 0x03


class Type(Enum):
    NONE = 0x00
    REL = 0x01
    EXEC = 0x02
    DYN = 0x03
    CORE = 0x04


class ISA(Enum):
    NONE = 0x00
    X86 = 0x03
    AMD64 = 0x3E
    Z80 = 0xDC


class ELF:
    def __init__(self, isa=ISA.NONE, type=Type.NONE, abi=ABI.LINUX):
        self.bitness = Bitness.BIT32
        self.endianness = Endianness.LITTLE
        self.abi = abi
        self.abi_version = 0
        self.type = type
        self.isa = isa
