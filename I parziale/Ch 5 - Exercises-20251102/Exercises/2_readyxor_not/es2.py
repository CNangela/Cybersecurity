import base64

def main():
    original = "El Psy Congroo"
    e_data = "IFhiPhZNYi0KWiUcCls="
    e_flag = "I3gDKVh1Lh4EVyMDBFo="

    d_data = base64.b64decode(e_data)
    b_data = ''.join(format(byte, '08b') for byte in d_data)
    b_original = ''.join(format(ord(c), '08b') for c in original)
    print(d_data)
    keystream = ''.join(str(int(x) ^ int(y)) for x, y in zip(b_data, b_original))
    print(keystream)

    d_flag = base64.b64decode(e_flag)
    b_flag = ''.join(format(byte, '08b') for byte in d_flag)
    b_flag = ''.join(str(int(x) ^ int(y)) for x, y in zip(b_flag, keystream))

    chars = [b_flag[i:i+8] for i in range(0, len(b_flag), 8)]
    text = ''.join(chr(int(b, 2)) for b in chars)
    print(text)



if __name__ == "__main__":
    main()