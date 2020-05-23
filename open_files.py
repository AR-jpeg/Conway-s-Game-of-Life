"""Open a file from 'starts'."""

def open_file(infile):
    """Open a file."""
    with open(infile) as f:
        out = f.read().split("\n")
        return out