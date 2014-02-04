#! /usr/bin/env python
# Time-stamp: <2014-02-03 15:56 christophe@pallier.org>

import glob, csv

def detectrep(f):
    dico = {}
    for w in f:
        if dico.has_key(w):
            print(w),
            dico[w] += 1
        else:
            dico[w] = 1

for f in glob.glob('list*.csv'):
    print("#### " + f)
    detectrep(open(f).readlines())
