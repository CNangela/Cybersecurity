# great; you've cleared the first step; i had to encrypt the message to prevent it from being intercepted. continue to decrypt;
import base64

def replace_chars(text, dict):
    replaced_text = ""
    for c in text: 
        replaced_text += dict.get(c, c)

    return replaced_text

def base64dec():
    value = "RmJ6cmd1dmF0IGpydmVxIHZmIHRidmF0IGJhIG5nIGd1ciB5dm9lbmVsLiBWIHpuYW50cnEgZ2IgdW5weCB2YWdiIG4gRWhmZnZuYSBzYmV6IFYgc2JoYXEgYmEgZ3VyIHl2b2VuZWwnZiBqcm9mdmdyLiBWIGd1dmF4IGd1cmwnZXIgaGZ2YXQgZ3VyIHl2b2VuZWwgbmYgbiBwYmlyZSBzYmUgemJlciBadmFxc3lubHJlIGVyZnJuZXB1LiBW4oCZeiB0YmFhbiB0dmlyIGxiaCBndXIgcGJiZXF2YW5ncmYgYnMgZ3VyIGZycGVyZyBjbmZmbnRyLCBncnl5IFp2eHIgZ2IgcGJ6ciB1cmVyIQoKNDUuNDExMzAwMTc5NjU1MDglMkMlMjAxMS44ODc3MzA3MjkyODExMTUlMjAxOS0xNi0xOC05LTIwLTI2JTdCMjAtOC01JTIwMTYtMTItMS0xNC0xMSVFMiU4MCU5OTE5JTIwMy0xNS0xNC0xOS0yMC0xLTE0LTIwJTIwOS0xOSUyMDIwLTgtNSUyMDExLTUtMjUlN0QKCjI5NjU2QzYyNjE3NDcyNkY2NjZENkY2MzIwNzQ2NTY3MjA2NDZFNjEyMDZCNkU2OTZDMjA2NTY4NzQyMDY1NzQ3MzYxNzAyODIwNDEzOTZDNjU3ODc3NkE0MTU5NUE1OTNENzYzRjY4NjM3NDYxNzcyRjZENkY2MzJFNjU2Mjc1NzQ3NTZGNzkyRTc3Nzc3NzJGMkYzQTczNzA3NDc0NjgyMDIxNjU2OTdBNzU1MzIwNzk2QzY1NzY2RjZDMjA3OTZEMjA2NDZFNjEyMDY1NkQyMDc5NjIyMDY0NjU2RDcyNkY2NjcyNjU3MDIwNjc2RTZGNzMyMDczNzM2NTZDNjQ2RTY1MjA2RTYxMjA2NTc2NzI2NTczNjU2NDIwNzU2Rjc5MjAyQzcyNjE2NjIwNzM2OTY4NzQyMDc0NjkyMDY1NjQ2MTZEMjA2NTc2Mjc3NTZGNzkyMDY2NDkyMDIxNzM2RTZGNjk3NDYxNkM3NTc0NjE3MjY3NkU2RjQz"
    decoded_bytes = base64.b64decode(value)
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text

solution = base64dec()
print (solution)

primo = "Fbzrguvat jrveq vf tbvat ba ng gur yvoenel. V znantrq gb unpx vagb n Ehffvna sbez V sbhaq ba gur yvoenel'f jrofvgr. V guvax gurl'er hfvat gur yvoenel nf n pbire sbe zber Zvaqsynlre erfrnepu. V’z tbaan tvir lbh gur pbbeqvangrf bs gur frperg cnffntr, gryy Zvxr gb pbzr urer!"
secondo = "45.41130017965508%2C%2011.887730729281115%2019-16-18-9-20-26%7B20-8-5%2016-12-1-14-11%E2%80%9919%203-15-14-19-20-1-14-20%209-19%2020-8-5%2011-5-25%7D"
terzo = "29656C626174726F666D6F632074656720646E61206B6E696C20656874206574736170282041396C6578776A41595A593D763F68637461772F6D6F632E65627574756F792E7777772F2F3A7370747468202165697A755320796C65766F6C20796D20646E6120656D2079622064656D726F6672657020676E6F73207373656C646E65206E61206576726573656420756F79202C7261662073696874207469206564616D20657627756F792066492021736E6F6974616C75746172676E6F43"

primo = primo.upper() 
print(primo)

dizionario_testo= {
    'V':'i',
    'N':'a',
    'A':'n',
    'T':'g',
    'R':'e',
    'Q':'d',
    'G':'t',
    'B':'o',
    'P':'c',
    'Y':'l',
    'U':'h',
    'X':'k',
    'E':'r',
    'O':'b',
    'S':'f',
    'C':'m',
    'J':'w',
    'F':'s',
    'I':'v',
    'H':'u',
    'L':'y',
    'Z':'m'}

print(f'traduzione: {replace_chars(primo,dizionario_testo)}')

cooridnate = "19-16-18-9-20-26-20-8-5-16-12-1-14-11-3-15-14-19-20-1-14-20-9-19-20-8-5-11-5-25"

cooridnate = cooridnate.split("-")
cord_text = ""
for i in cooridnate:
    cord_text += chr(ord('a')+int(i)-1)
print (cord_text)

#flag : spritztheplankconstantisthekey

hex = "29656C626174726F666D6F632074656720646E61206B6E696C20656874206574736170282041396C6578776A41595A593D763F68637461772F6D6F632E65627574756F792E7777772F2F3A7370747468202165697A755320796C65766F6C20796D20646E6120656D2079622064656D726F6672657020676E6F73207373656C646E65206E61206576726573656420756F79202C7261662073696874207469206564616D20657627756F792066492021736E6F6974616C75746172676E6F43"
bytes_string = bytes.fromhex(hex)
ascii_string = bytes_string.decode("ascii")
print(ascii_string)

ascii_string_reverse = ascii_string[::-1]
print(ascii_string_reverse)

