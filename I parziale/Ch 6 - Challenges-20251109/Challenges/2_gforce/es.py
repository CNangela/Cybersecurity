import base64

def main():
    val = "SU5TQXtjMTgwN2EwYjZkNzcxMzI3NGQ3YmYzYzY0Nzc1NjJhYzQ3NTcwZTQ1MmY3N2I3ZDIwMmI4MWUxNDkxNzJkNmE3fQ=="

    # decodifica in byte
    decoded_bytes = base64.b64decode(val)

    # converti i byte in stringa
    decoded_string = decoded_bytes.decode('utf-8')

    print(decoded_string)


if __name__ == "__main__":
    main()