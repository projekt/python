#!/usr/bin/env python3
# iznad je shebang za moj sistem
# join link: https://replit.com/join/txfktylslg-srdjanljustina
# import paketa 
import io
import sys
# -*- coding: utf-8 -*-

# unos igraca
igrac1 = []
igrac2 = []

igrac1 = [int(item) for item in input("Unesite karte za prvog igrača : ").split(',')]
igrac2 = [int(item) for item in input("Unesite karte za drugog igrača : ").split(',')]

# da li je broj karata isti
if len(igrac1)!=len(igrac2):
	print('Unos nije ispravan!')
	sys.exit(0)

# ispis karti za igrace

print('(',str(igrac1)[1:-1],')')
print('(',str(igrac2)[1:-1],')')

# nova linija za lepsi ispis
print('')


# petlja koja znaci bacanje,ruku
for i in range(len(igrac1)):
    if (igrac1[i]==igrac2[i]):
        print('(',igrac1[i],',', igrac2[i], ')',sep='',end=''),

    if (igrac1[i]>igrac2[i]):
        print('(X', ',' ,igrac2[i], ')',sep='',end=''),

    if (igrac1[i]<igrac2[i]): 
       print('(',igrac1[i],',', 'X', ')',sep='',end=''),

# nova linija 
print('')


