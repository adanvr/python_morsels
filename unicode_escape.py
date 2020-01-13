from argparse import ArgumentParser, FileType

def escape(character, style):
    code = ord(character)
    if code <= 127:
        return character
    elif style == "html":
        return f"&#{hex(code)[1:]};"
    elif code > 0xffff:
        return rf"\U{hex(code)[2:]:0>8}"
    else:
        return rf"\u{hex(code)[2:]:0>4}"

def escape_file(text_file, style):
    contents = text_file.read()
    return ''.join(
        escape(c, style)
        for c in contents
    )

def main():
    parser = ArgumentParser()
    parser.add_argument('file', type=FileType('rt'))
    parser.add_argument(
        '--style',
        choices=['default', 'html'],
        default='default',
    )
    args = parser.parse_args()
    print(escape_file(args.file, style=args.style), end='')

if __name__ == "__main__":
    main()