from enum import Enum


class Bitness(Enum):
    BIT32 = 0x01
    BIT64 = 0x02


class Endianness(Enum):
    LITTLE = 0x01
    BIG = 0x02


class ABI(Enum):
    SYSTEM_V = 0x00
    HP_UX = 0x01
    NETBSD = 0x02
    LINUX = 0x03
    GNU_HURD = 0x04
    SOLARIS = 0x06
    AIX = 0x07
    IRIX = 0x08
    FREEBSD = 0x09
    TRU64 = 0x0A
    NOVELL_MODESTO = 0x0B
    OPENBSD = 0x0C
    OPENVMS = 0x0D
    NONSTOP_KERNEL = 0x0E
    AROS = 0x0F
    FENIX_OS = 0x10
    CLOUD_ABI = 0x11
    OPENVOS = 0x12


class ISA(Enum):
    NONE = 0x00
    X86 = 0x03
    AMD64 = 0x3e
    Z80 = 0xdc


class ELF:
    pass
