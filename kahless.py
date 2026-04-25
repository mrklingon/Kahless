import time
import random

pics = ["bird","blade","D7","fleet","ship","warbird","emblem"]

def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1


def wisdom(num,filename):
    qs = open(filename)
    for i in range(num+1):
        quote = qs.readline()
    qs.close()
    return quote

def cat(file):
    l = file_len(file)
    for ln in range(l):
        print(wisdom(ln,file).rstrip())

def getWD(fnm):
    len = file_len(fnm)
    line = wisdom(random.randrange(len),fnm)
    line = line.strip("\n");
    return ( line   )  

def swisdom(filename,srch):
    x = file_len(filename)
    qs= open(filename)
    for i in range(x):
        t = qs.readline().rstrip()
        if t.lower().find(srch.lower()) >= 0:
            print(t+"\n")

    qs.close()

cat("emblem")

while True:
    print("\n-------------\nWhat do you want to search for in the Kahless lexicon?")
    s = input()
    print("\n")
    swisdom("kahless.txt",s)
    time.sleep(6)
    cat(random.choice(pics))
    print(getWD("worf"))
