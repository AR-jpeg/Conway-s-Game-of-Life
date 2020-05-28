"""Open a file from 'starts'."""

def open_file(infile):
    """Open a file."""
    with open(infile) as f:
        out = f.read().split("\n")
        end = []

        for i in out:
            i = i.split()
            print(i)
            end.append((int(i[0]), int(i[1])))

        return end