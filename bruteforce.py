import sys
import os
import argparse
import base64
from hashlib import *

def password_crack():
    config = argument_parser()

    # 
    if(config['hash']):
        hash_path = config['hash']
        f = open(hash_path, 'r')
        for i in f:
            hash = i.strip(); 
        f.close()
    
    try:
        if(config['file']):
            f = open(config['file'], 'r')
            for line in f:
                value = line.strip()
                print("Testing {} against {}".format(value, hash))
                data = md5(value.encode("utf-8")).hexdigest()
                if(str(data) == str(hash)):
                    print("Match found: {}".format(line))
                    sys.exit()
    except KeyError:
        print("Please specify a path to the pass file.")

def determine_hash(value):
    # initialize argument parser
    config = argument_parser()
    # if algorithm argument is MD5
    if(config['algorithm']=='MD5'):
        data = md5(value.encode()).hexdigest()
    # if algorithm is SHA1
    elif(config['algorithm']=='SHA1'):
        data = sha1(value.encode()).hexdigest()
    # otherwise, encode in base64
    else:
        data = base64.b64encode(value)
    return(data)

def argument_parser():
    # Initializing argument parser / parser title
    parser = argparse.ArgumentParser(description="Value Decoder/Hash Cracker developed by DaZ", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # Adding arguments to script
    parser.add_argument('-f', '--file', type=str, help="Wordlist", default=argparse.SUPPRESS)
    # TODOparser.add_argument('-t', '--threads', type=int, help="Specify thread value for hash cracking", default="3")
    parser.add_argument('algorithm', help="algorithm of hash", default="Base64")
    parser.add_argument('hash', type=str, help="file/path containing encoded value", default=argparse.SUPPRESS)
    # Condensing args for configuration to be called in any other function
    args = parser.parse_args()
    config = vars(args)
    return(config)

def main():
    # run script
    print('WELCOME {0} TO PASSWORD CRACKER'.format(os.getenv('USER') or os.getenv('USERNAME')))
    password_crack()
    
main()

