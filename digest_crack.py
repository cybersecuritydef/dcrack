import getopt
import sys
import hashlib

def help():
    print("Help")

    
def digest_auth_crack(info):
    password = None
    if
    with open(info["wordlist"], "r", encoding='utf-8') as f:        
        for line in f:
            ha1 = hashlib.md5('{}:{}:{}'.format(info["username"], info["realm"], line.strip()).encode())        
            ha2 = hashlib.md5('{}:{}'.format(info["method"], info["url"]).encode())
            ha3 = hashlib.md5('{}:{}:{}:{}:{}:{}'.format(ha1.hexdigest(), info["nonce"], info["nc"], info["cnonce"], info["qop"], ha2.hexdigest()).encode())
            if info["response"] == ha3.hexdigest():
                password = line.strip()                
                break
    return password


def main():
    data = dict()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "wordlist=", "username=", "realm=", "nonce=", "url=", "nc=", "cnonce=", "qop=", "method=", "response="])
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                help()
                sys.exit(0)
            elif opt == "--wordlist":
                data["wordlist"] = arg
            elif opt == "--username":
                data["username"] = arg
            elif opt == "--realm":
                data["realm"] = arg
            elif opt == "--nonce":
                data["nonce"] = int(arg)
            elif opt == "--url":
                data["url"] = arg
            elif opt == "--nc":
                data["nc"] = arg
            elif opt == "--cnonce":
                data["cnonce"] = arg
            elif opt == "--qop":
                data["qop"] = arg
            elif opt == "--method":
                data["method"] = arg
            elif opt == "--response":
                data["response"] = arg
        if len(data) == 10:         
            print("\n[!] Starting crack...\n")
            pwd = digest_auth_crack(data)
            if pwd is not None:
                print('[+] Found!: {}\n'.format(pwd))
            print("[+] Finished crack!")
        else:
            print("ELSE {}".format(data))
    except getopt.GetoptError as err:
        print(err)
        sys.exit(0)


if __name__ == "__main__":
    main()
