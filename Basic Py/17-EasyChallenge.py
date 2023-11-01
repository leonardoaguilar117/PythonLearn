def read_write(toRead, toWrite):
    with open(toWrite, "w") as text2:
        with open(toRead, "r") as text:
            for line in text:
                if not (line.startswith('#') or (line.startswith('"""') and line.endswith('"""'))):
                    text2.write(line)
    text.close()
    text2.close()
