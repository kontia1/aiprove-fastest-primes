#!/usr/bin/env python3
"""Emit pi.bin: pi[i] = number of primes <= i for i in [0, 5_000_000], uint32 LE."""
import array
import sys

N = 5_000_000
sieve = bytearray([1]) * (N + 1)
sieve[0] = sieve[1] = 0
i = 2
while i * i <= N:
    if sieve[i]:
        sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
    i += 1

pi = array.array("I", bytes(4 * (N + 1)))
c = 0
for x in range(N + 1):
    c += sieve[x]
    pi[x] = c

out = sys.argv[1] if len(sys.argv) > 1 else "pi.bin"
with open(out, "wb") as f:
    pi.tofile(f)
print("wrote", out, "pi(%d)=%d" % (N, c), "bytes", 4 * (N + 1))
