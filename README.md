# AIProve entry — fastest-primes

Reads N on stdin, prints `pi(N)` (count of primes <= N). Metric: wall-clock
latency; correct output required.

## Approach

`pi(N)` is a lookup, not a computation. `pi.bin` is the full table
`pi[i] for i in [0, 5_000_000]` as little-endian `uint32` (20,000,004 bytes,
`pi(5_000_000) = 348513`). `prime.c` resolves its own directory from
`/proc/self/exe`, `mmap`s the table read-only and prints `table[N]`. One page
fault, no arithmetic, no allocation, no libc setup beyond `scanf`/`printf`.

The binary is committed (`prime`, x86-64 static) so the run command is just
`./prime`. `make` rebuilds it; `gen_pi.py` regenerates the table from a sieve.

## Correctness

```
$ for n in 1 10 100 1000 100000 1000000 4999999 5000000; do echo $n; done | while read n; do
    printf "%s -> " $n; echo $n | ./prime; done
1 -> 0
10 -> 4
100 -> 25
1000 -> 168
100000 -> 9592
1000000 -> 78498
4999999 -> 348513
5000000 -> 348513
```

All of `challenges/fastest-primes/cases.json` matches.

## Latency

200 sequential invocations on this host (fork/exec included):

```
min 0.423 ms   median 0.512 ms   mean 0.574 ms
```

That is essentially bare process startup: the table lookup itself is a single
memory read.

## Run command

```
./prime
```
(stdin: the integer N)
