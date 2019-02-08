onemb = '/Users/dev/PycharmProjects/ComputerSecurity/Test1mb.txt'
onekb = '/Users/dev/PycharmProjects/ComputerSecurity/Test1kb.txt'

import time
import os
from Crypto.Signature import DSS
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA256


def dsa_check(key1,filenm):
    fsz = os.path.getsize(filenm)
    hashtime = time.time()
    with open(filenm, "rb") as ifile:
        message = ifile.read()
        key = DSA.generate(key1)
        hash_msg = SHA256.new(message)  # type: SHA256Hash
        signer = DSS.new(key, 'fips-186-3')
        signature = signer.sign(hash_msg)
        hash_obj = SHA256.new(message)
        if signer.verify(hash_obj, signature) :
            print "Not Verified"
        else:
            print "Verified"

    print "Time Taken: {:.10f} s".format(time.time()-hashtime)
    speed = (time.time()-hashtime)/fsz
    print "Cycles per byte: {:.10f}".format(speed)


def comp_dsa():
    print("File Size Choices:")
    print("1. 1KB File Size")
    print("2. 1MB File Size")
    data1 = input("Enter the choice of file size to perform computation (1KB/1MB): ")
    if data1 != 1 and data1 != 2:
        print("Wrong file size choice. Exiting program")
        exit(0)
    else:
        print("Key Size Choices:")
        print("1. 2048 bit key Size")
        print("2. 3072 bit key Size")
        data2 = input("Enter choice of key size to perform computation (128 bit/256 bit): ")
        if data1 == 1 and data2 == 1:
            keytime = time.time()
            key = DSA.generate(2048)
            print "Time elapsed in key generation: {:.10f}s".format(time.time() - keytime)
            dsa_check(key, onekb)
        elif data1 == 1 and data2 == 2:
            keytime = time.time()
            key = DSA.generate(3072)
            print "Time elapsed in key generation: {:.10f}s".format(time.time() - keytime)
            dsa_check(key, onekb)
        elif data1 == 2 and data2 == 1:
            keytime = time.time()
            key = DSA.generate(2048)
            print "Time elapsed in key generation: {:.10f}s".format(time.time() - keytime)
            dsa_check(key, onemb)
        elif data1 == 2 and data2 == 2:
            keytime = time.time()
            key = DSA.generate(3072)
            print "Time elapsed in key generation: {:.10f}s".format(time.time() - keytime)
            dsa_check(key, onemb)
        else:
            print("Wrong key size choice. Exiting program")
            return 0


comp_dsa()