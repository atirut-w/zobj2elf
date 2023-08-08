from enum import Enum
from io import BufferedReader


def load_string(file: BufferedReader) -> str:
    length = int.from_bytes(file.read(1), "little")
    return file.read(length).decode("ascii")


def load_lstring(file: BufferedReader) -> str:
    length = int.from_bytes(file.read(2), "little")
    return file.read(length).decode("ascii")


class ExpressionType(Enum):
    END = chr(0)

    UINT8 = "U"
    INT8 = "S"
    UINT8_EXT = "u"
    INT8_EXT = "s"
    INT16_LE = "C"
    INT16_BE = "B"
    INT24 = "P"
    INT32 = "L"

    REL_JMP = "J"
    REL_FF00 = "H"
    COMPUTED = "="


class ModuleNameScope(Enum):
    END = chr(0)
    LOCAL = "L"
    GLOBAL = "G"


class ModuleNameType(Enum):
    RELOC_ADDR = "A"
    CONSTANT = "C"
    COMPUTED = "="


class ModuleName:
    def __init__(self, file: BufferedReader):
        self.scope: ModuleNameScope = ModuleNameScope(file.read(1).decode("ascii"))
        if self.scope == ModuleNameScope.END:
            return

        self.type: ModuleNameType = ModuleNameType(file.read(1).decode("ascii"))
        self.section = load_lstring(file)
        self.value = int.from_bytes(file.read(4), "little")
        self.name = load_lstring(file)
        self.file_name = load_lstring(file)
        self.line = int.from_bytes(file.read(4), "little")


class Expression:
    def __init__(self, file: BufferedReader):
        self.type: ExpressionType = ExpressionType(file.read(1).decode("ascii"))
        if self.type == ExpressionType.END:
            return

        self.source_file = load_lstring(file)
        self.line = int.from_bytes(file.read(4), "little")
        self.section = load_lstring(file)
        self.rel_instruction_offset = int.from_bytes(file.read(4), "little")
        self.patch_offset = int.from_bytes(file.read(4), "little")
        self.opcode_size = int.from_bytes(file.read(4), "little")
        self.target_name = load_lstring(file)
        self.expression = load_lstring(file)


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

        file.seek(module_name_offset)
        self.module_name = load_lstring(file)

        file.seek(expressions_offset)
        self.expressions: list[Expression] = []

        for _ in range(2048):
            exp = Expression(file)

            if exp.type == ExpressionType.END:
                break
            elif exp.source_file == "":
                exp.source_file = self.expressions[-1].source_file

            self.expressions.append(exp)

        file.seek(module_names_offset)
        self.module_names: list[ModuleName] = []

        for _ in range(2048):
            modname = ModuleName(file)
            if modname.scope == ModuleNameScope.END:
                break

            self.module_names.append(modname)
        
        file.seek(external_names_offset)
        self.external_names: list[str] = []

        for _ in range(2048):
            name = load_lstring(file)
            if name == "":
                break # TODO: Confirm with Z88DK devs if this is correct

            self.external_names.append(name)

    @property
    def version(self) -> int:
        return int(self.signature[6:8])
