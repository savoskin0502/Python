import argparse
import os
import tempfile
import json
from io import StringIO
from functools import reduce

def conc(a, b):
    return a + ", " + b

def write_json(data, filename): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="key for storage")
    parser.add_argument("--val", help="value for storage")
    args = parser.parse_args()
    # print(tempfile.gettempdir())
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    # print(storage_path)

    if (not os.path.exists(storage_path)):
        with open(storage_path, 'w') as f:
            json.dump({}, f)
    
    if (args.key and args.val):
        with open(storage_path) as f:
            data = json.load(f)
            all_keys = data.keys()
            key_exist = False
            for key in all_keys:
                if (key==args.key):
                    key_exist = True
            
            if (not key_exist):
                data[args.key] = [args.val]
                write_json(data, storage_path)
            else:
                data[args.key].append(args.val)
                write_json(data, storage_path)
    elif(args.key and not args.val):
        with open(storage_path) as f:
            data = json.load(f)
            all_keys = data.keys()
            key_exist = False
            for key in all_keys:
                if (key==args.key):
                    key_exist = True

            if key_exist:
                s = reduce(conc, data[args.key])
                print(s)
            else:
                print(None)
