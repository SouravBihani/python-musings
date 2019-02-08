# author - pagarwal@buffalo.edu

import os, random, struct
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
import time

in_filename = '/Users/dev/PycharmProjects/ComputerSecurity/Priority_donation.txt'
out_filename = '/Users/dev/PycharmProjects/ComputerSecurity/verify.txt'
fsz = os.path.getsize(in_filename)
iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(8))


def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    encrtime = time.time()
    if not out_filename:
        out_filename = in_filename + '.enc'

    ctr_e = Counter.new(64, prefix=iv)
    encryptor = AES.new(key, AES.MODE_CTR, counter=ctr_e)
    filesize = os.path.getsize(in_filename)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))
    print "Time elapsed for encryption: {:.10f} s".format(time.time() - encrtime)
    speedencr = fsz / encrtime
    print "Speed per byte: {}".format(speedencr)


def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):

    decrtime = time.time()
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        ctr_d = Counter.new(64, prefix=iv)
        decryptor = AES.new(key, AES.MODE_CTR, counter=ctr_d)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                outfile.write(decryptor.decrypt(chunk))

    print "Time elapsed for decryption: {:.10f} s".format(time.time() - decrtime)
    speedencr = fsz / decrtime
    print "Speed per byte: {}".format(speedencr)


def aescode():
    print "File Size: {} bytes".format(fsz)
    data = input("Enter the size of key in bytes (16/32): ")
    # 256 bit key
    if data == 32:
        keytime1 = time.time()
        keys = Random.new().read(data)[:32]
        print "Time elapsed for key generation: {:.10f} s".format(time.time() - keytime1)
        encrypt_file(keys, in_filename, out_filename, 32)
        decrypt_file(keys, in_filename, out_filename, 32)
    # 128 bit key
    elif data == 16:
        keytime2 = time.time()
        keys = Random.new().read(data)[:16]
        print "Time elapsed for key generation: {:.10f} s".format(time.time() - keytime2)
        encrypt_file(keys, in_filename, out_filename, 16)
        decrypt_file(keys, in_filename, out_filename, 16)
    else:
        print("Wrong key size entered. Exiting program")
        # break

aescode()