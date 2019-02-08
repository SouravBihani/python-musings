import hashlib
from Crypto.Hash import SHA3_256
import time
import os

block = 6553665536
onemb = '/Users/dev/PycharmProjects/ComputerSecurity/Test1mb.txt'
onekb = '/Users/dev/PycharmProjects/ComputerSecurity/Test1kb.txt'


def sha256_hash(in_filename):
    fsz = os.path.getsize(in_filename)
    hashtime = time.time()
    hashobj = hashlib.sha256()
    with open(in_filename,'rb') as afile:
        buff = afile.read(block)
        while len(buff) > 0 :
            hashobj.update(buff)
            buff = afile.read(block)
    print (hashobj.hexdigest())
    print "Time elapsed : {:.10f}s".format(time.time() - hashtime)
    speed = (time.time() - hashtime)/fsz
    print "Cycles per Byte: {:.10f}".format(speed)


def sha512_hash(in_filename):
    fsz = os.path.getsize(in_filename)
    hashtime = time.time()
    hashobj = hashlib.sha512()
    with open(in_filename, 'rb') as afile:
        buff = afile.read(block)
        while len(buff) > 0:
            hashobj.update(buff)
            buff = afile.read(block)
    print (hashobj.hexdigest())
    print "Time elapsed : {:.10f}s".format(time.time() - hashtime)
    speed = (time.time() - hashtime)/fsz
    print "Cycles per Byte: {:.10f}".format(speed)


def sha3256_hash(in_filename):
    fsz = os.path.getsize(in_filename)
    hashtime = time.time()
    hashobj = SHA3_256.new()
    with open(in_filename,'rb') as afile:
        buff = afile.read(block)
        while len(buff) > 0 :
            hashobj.update(buff)
            buff = afile.read(block)
    print (hashobj.hexdigest())
    print "Time elapsed : {:.10f}s".format(time.time() - hashtime)
    speed = fsz / hashtime
    print "Cycles per Byte: {:.10f}".format(speed)


def compute_hash():
    print("Hash Algorithm Choices: (1/2/3) ")
    print("1. SHA 256")
    print("2. SHA 512")
    print("3. SHA 3-256")
    data = input("Please enter the choice: ")
    if data == 1:
        print("The Hash is for 1KB file is: ")
        sha256_hash(onekb)
        print(" ")
        print("The Hash is for 1MB file is: ")
        sha256_hash(onemb)
    elif data == 2:
        print("The Hash is for 1KB file is: ")
        sha512_hash(onekb)
        print(" ")
        print("The Hash is for 1MB file is: ")
        sha512_hash(onemb)
    elif data == 3:
        print("The Hash is for 1KB file is: ")
        sha3256_hash(onekb)
        print(" ")
        print("The Hash is for 1MB file is: ")
        sha3256_hash(onemb)
    else:
        print("Invalid choice. Exiting program")
        return 0


compute_hash()