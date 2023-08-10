from enum import Enum


class Bitness(Enum):
    BIT32 = 0x01
    BIT64 = 0x02


class Endianness(Enum):
    LITTLE = 0x01
    BIG = 0x02


class ABI(Enum):
    LINUX = 0x03


class ISA(Enum):
    NONE = 0x00
    X86 = 0x03
    AMD64 = 0x3e
    Z80 = 0xdc


class ELF:
    pass
