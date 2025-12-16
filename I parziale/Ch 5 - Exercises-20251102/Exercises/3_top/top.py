#!/usr/bin/env python3
import random
import sys
import time

cur_time = str(time.time()).encode('ASCII')
random.seed(cur_time)

print(cur_time)

msg = 'ciao'.encode('ASCII')
key = [random.randrange(256) for _ in msg]
c = [m ^ k for (m,k ) in zip(msg + cur_time, key + [0x88]*len(cur_time))]

with open("top_secret", "rb") as f:
    secret = f.read()
print(len(secret))

sec_time = secret[-len(cur_time):]
plain_time = ''.join([chr(m ^ k) for (m, k) in zip(sec_time, [0x88]*len(cur_time))])
print(f"plain time:\t{plain_time}")

random.seed(plain_time.encode("ASCII"))

#get the keys
keys_secret = [random.randrange(256) for _ in secret[:-len(cur_time)]]
plain_text = ''.join([chr(m ^ k) for (m, k) in zip(secret[:-len(cur_time)], keys_secret)])
print(plain_text)