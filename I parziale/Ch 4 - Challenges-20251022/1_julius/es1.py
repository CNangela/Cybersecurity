import base64

def main():
    str1 = "Q2Flc2FyCg=="
    str2 = "fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=="

    str1encoded = base64.b64decode(str1).decode()
    str2encoded = base64.b64decode(str2).decode('utf-8', errors="ignore")
    print(str1encoded)
    print(str2encoded)

    for i in range(-30, 30): 
        curr_step = ''.join([chr(ord(c) + i) for c in str2encoded])

        print(f"Step={i}\t{curr_step}")


if __name__ == "__main__":
    main()