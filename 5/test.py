import json, re, base64

def get_str(path=None):
    if path is None:
        return

    print('start')
    
    f = open(path)
    f = f.read()
    for line in f:
        print(base64.b64decode(line).decode('utf-8'))

def get_json(path=None):
    if path is None:
        return

    print('start')
    
    f = open(path)
    f = f.read()
    if(not f.startswith('[')):
        f = '[' + f
        print('done with [')

    if(not f.endswith('[')):
        f = f + ']'
        print('done with ]')

    f = re.sub('}[\n]?{', '},{', f)
    print('done with }{')

    return f

def read_file(path=None):
    if path is None:
        return

    print('start read_file')
    f = open(path)
    return f.read()
    print('done read_file')

    
def find_ip(path=None):
    if path is None:
        return

    s = read_file(path)
    print('start find_ip')

    f = re.findall(r'[0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3}', s)
    f = list(set(f))
    #f = [a for a in f if a not in ('4.0.0.0', '224.0.0.251', '239.255.255.250', '127.0.0.1', '192.168.1.1', '255.255.255.255', '0.0.0.0', '224.0.0.252')]
    f = f.sort()
    print('done find_ip')
    return f


if __name__ == '__main__':
    p = r'C:\Users\redmo\Documents\Study\Uni\9\Data_Protection_Against_Unauthorized_Access\Labs\5\sample.json'

    
    print(find_ip(p))
