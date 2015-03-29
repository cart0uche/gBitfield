#!/usr/bin/env python

import json
import bitstring


def load_config():
    json_data = open('config.json').read()
    bitfields = json.loads(json_data)
    return bitfields

if __name__ == "__main__":
    bitfields = load_config()

    inst = bitfields['bitfields'][0]['fields'][0]['size'],  bitfields['bitfields'][0]['fields'][1]['size']
    print inst
    a = bitstring.pack(inst, 3, 2)
    print a.bin
