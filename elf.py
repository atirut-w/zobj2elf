from enum import Enum
from io import BufferedWriter


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
        self.version = 1
        self.abi = abi
        self.abi_version = 0
        self.type = type
        self.isa = isa
        self.entry_point = 0
        self.flags = 0

    def write(self, file: BufferedWriter):
        file.write(b"\x7FELF")
        file.write(bytes([self.bitness.value]))
        file.write(bytes([self.endianness.value]))
        file.write(bytes([self.version]))
        file.write(bytes([self.abi.value]))
        file.write(bytes([self.abi_version]))
        file.write(b"ELFROCK")  # :D
        self.__write_int(file, self.type.value, 2)
        self.__write_int(file, self.isa.value, 2)
        self.__write_int(file, self.version, 4)
        self.__write_int(
            file, self.entry_point, 4 if self.bitness == Bitness.BIT32 else 8
        )

        phoff = file.tell()
        self.__write_int(file, 0, 4 if self.bitness == Bitness.BIT32 else 8)

        shoff = file.tell()
        self.__write_int(file, 0, 4 if self.bitness == Bitness.BIT32 else 8)

        self.__write_int(file, self.flags, 4)
        self.__write_int(file, 52 if self.bitness == Bitness.BIT32 else 64, 2)

        self.__write_int(file, 0x20 if self.bitness == Bitness.BIT32 else 0x38, 2)
        self.__write_int(file, 0, 2)  # TODO: Write program headers

        self.__write_int(file, 0x28 if self.bitness == Bitness.BIT32 else 0x40, 2)
        self.__write_int(file, 0, 2)  # TODO: Write section headers

        self.__write_int(file, 0, 2)  # TODO: Write string table index

    def __write_int(self, file: BufferedWriter, value: int, size: int):
        file.write(
            value.to_bytes(
                size, "little" if self.endianness == Endianness.LITTLE else "big"
            )
        )
