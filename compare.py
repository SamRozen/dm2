#! /usr/bin/env python

import sys
import tempfile


def load_file(filename):
    with open(filename) as f:
        res = set(map(lambda x: x.strip('" \'\n').lower(), f.readlines()))
    return res


def write_set(s):
    f = tempfile.NamedTemporaryFile(mode='w+b', delete=False)
    f.writelines('\n'.join(sorted(s)))
    f.close()
    return f.name


s1 = load_file(sys.argv[1])
s2 = load_file(sys.argv[2])

s1_and_s2 = s1 & s2

print('S1: ', len(s1), write_set(s1))
print('S2: ', len(s2), write_set(s2))
print('S1 & S2:', len(s1_and_s2), write_set(s1_and_s2))
