import base64
from Crypto.Cipher import AES

def main():

    data = "jewAMcx4zd5R4dRrRvg6D3K23WcHTPONX9rI6gp4b5HECz62JjwJO74JXHdfGpomQtttTt2oOO7I7b0DsfFa5oI9MS3yHWN/Mv2DlgTRW71tFste1pXi7Q5kk/JcyFZbqpOmqtSWQyXmvUX1scF/G3tkmScWABkfsf+Rvl5umULqdohT9O6r40Y/hCFbC78XuOc6HeJ+jPgUSa/rm8eauUT6YDOAwMsxyIQ2nRQEd4c9Wja7MZrLOsvOZCp5gtmUJNIc1y0O1R/6PaVu9I6lUrIqi3Z+KgTDqyXTBBGUUK7JNtqxojcdlsJZEgjTvg/u6Q1BcV9gkd0gqxIyz0mb9A=="

    decoded_bytes = base64.b64decode(data)

    print(decoded_bytes)  

    # serve la chiave e IV corretti
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(decoded_bytes)


if __name__ == "__main__":
    main()