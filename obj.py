from io import BufferedReader


def load_string(file: BufferedReader) -> str:
    length = int.from_bytes(file.read(1), "little")
    return file.read(length).decode("ascii")


def load_lstring(file: BufferedReader) -> str:
    length = int.from_bytes(file.read(2), "little")
    return file.read(length).decode("ascii")


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

    @property
    def version(self) -> int:
        return int(self.signature[6:8])
