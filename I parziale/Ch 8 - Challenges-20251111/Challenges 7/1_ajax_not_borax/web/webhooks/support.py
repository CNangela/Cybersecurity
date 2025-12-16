import base64

def main():
    val = "ZmxhZ3tzZDkwSjBkbkxLSjFsczlISmVkfQ=="

    # decodifica in byte
    decoded_bytes = base64.b64decode(val)

    # converti i byte in stringa
    decoded_string = decoded_bytes.decode('utf-8')

    print(decoded_string)
    #per trovare da md5, usa https://crackstation.net

if __name__ == "__main__":
    main()