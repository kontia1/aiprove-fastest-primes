CC ?= gcc
CFLAGS ?= -O2 -static

prime: prime.c
	$(CC) $(CFLAGS) -o prime prime.c

pi.bin:
	python3 gen_pi.py pi.bin

clean:
	rm -f prime
