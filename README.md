# ticfile

A library for reading and writing TIC-80 .tic cartridge files.

See https://github.com/nesbox/TIC-80/wiki/.tic-File-Format for the file format description.

## Installation

```sh
pip install ticfile
```

## Usage

```python
from ticfile import TICFile, ChunkType

duck_jam = TICFile.open("duckjam.tic")
code_chunks = [chunk for chunk in duck_jam.chunks if chunk.type == ChunkType.CODE]
code_lines = code_chunks[0].data.decode("ascii").split("\n")
print(code_lines[0])
```

## API

The `ticfile` module provides the following definitions:

### TICFile

Represents a complete .tic file.

#### Class methods

* `TICFile(chunks)` - construct a `TICFile` from a list of `Chunk` objects
* `TICFile.open(filename)` - open a `TICFile` from the given filename
* `TICFile.from_file(f)` - open a `TICFile` from the given file handle

#### Instance methods / attributes

* `chunks` - the list of `Chunk` objects making up this file
* `save(filename)` - write this file to the given filename

### ChunkType

An enum defining the available chunk types:

```python
ChunkType.TILES = 1
ChunkType.SPRITES = 2
ChunkType.MAP = 4
ChunkType.CODE = 5
ChunkType.FLAGS = 6
ChunkType.SAMPLES = 9
ChunkType.WAVEFORM = 10
ChunkType.PALETTE = 12
ChunkType.MUSIC = 14
ChunkType.PATTERNS = 15
ChunkType.DEFAULT = 17
ChunkType.SCREEN = 18
ChunkType.BINARY = 19
ChunkType.COVER_DEP = 3
ChunkType.PATTERNS_DEP = 13
ChunkType.CODE_ZIP = 16
```

### Chunk

Represents an individual chunk within a .tic file.

#### Class methods

* `Chunk(chunk_type, bank, data)` - construct a `Chunk` object
** `chunk_type` - one of the enum values defined in `ChunkType`
** `bank` - the bank number (0..7) for this chunk
** `data` - the binary data of this chunk, excluding the header, as a `bytes` object

### Instance methods / attributes

* `type` - the type of this chunk, given as one of the enum values defined in `ChunkType`
* `bank` - the bank number (0..7) for this chunk
* `data` - the binary data of this chunk, excluding the header, as a `bytes` object
* `write(f)` - write this chunk to the given file handle
