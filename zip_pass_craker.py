#this code implements threading

import zipfile
import optparse
from threading import Thread

def extractFile(zfile,password):
    try:
        zfile.extractall(pwd=password)
        print '[+] Found Password ' + password + '\n'
    except:
        pass

def main():
    parser = optparse.OptionParser("usage%prog"+" -f <zipfile> -d <dictonary>")
    parser.add_option('-f',dest='zname',type='string',help='specify zip file')
    parser.add_option('-d', dest= 'dname', type='string', help='specify sictonary file')
    (options, args)= parser.parse_args()
    if(options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zfile = zipfile.ZipFile(zname)
    passFIle = open(dname)
    for line in passFIle.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile(zfile,password))
        t.start()
if __name__ == '__main__':
    main()
