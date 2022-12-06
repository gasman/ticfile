from enum import Enum
import struct

class ChunkType(Enum):
    TILES = 1
    SPRITES = 2
    MAP = 4
    CODE = 5
    FLAGS = 6
    SAMPLES = 9
    WAVEFORM = 10
    PALETTE = 12
    MUSIC = 14
    PATTERNS = 15
    DEFAULT = 17
    SCREEN = 18
    BINARY = 19
    COVER_DEP = 3
    PATTERNS_DEP = 13
    CODE_ZIP = 16


class Chunk:
    def __init__(self, chunk_type, bank, data):
        self.type = chunk_type
        self.bank = bank
        self.data = data

    def write(self, f):
        t = (self.bank << 5) | self.type.value
        f.write(
            struct.pack("<BHx", t, len(self.data))
        )
        f.write(self.data)

    def __repr__(self):
        return "<Chunk %s (len %d)>" % (self.type.name, len(self.data))


class TICFile:
    @staticmethod
    def open(filename):
        with open(filename, "rb") as f:
            return TICFile.from_file(f)

    @staticmethod
    def from_file(f):
        chunks = []

        while True:
            header_bin = f.read(4)
            if len(header_bin) == 0:
                break
            elif len(header_bin) != 4:
                raise Exception("Invalid .tic file")

            t, size = struct.unpack("<BHx", header_bin)
            chunk_type = ChunkType(t & 0x1f)
            bank = t >> 5
            data = f.read(size)
            if len(data) != size:
                raise Exception("Invalid .tic file")

            chunks.append(
                Chunk(chunk_type, bank, data)
            )

        return TICFile(chunks)

    def __init__(self, chunks):
        self.chunks = chunks

    def save(self, filename):
        with open(filename, "wb") as f:
            for chunk in self.chunks:
                chunk.write(f)

    def __repr__(self):
        return "<TICFile: %r>" % self.chunks
