# The idea:

Implement RSA in python 

RSA can be split into 4 main steps
- key generation
	- key generation is split into 2 parts. The generation of a public and 
		a private key. 
	- both private and public key are generated from 2 (typically enormous) prime numbers.
	- The private key is d where e ✕ d = 1(mod(p-1)(q-1)) i.e d = 1(mod(p-1)(q-1)) / d
		- There where some difficulties in this section in calculating the values of d
	- The public key is N where N = pq and another number e.
- key distribution
	- The public key is given to whomever you want. Remember the the public key is 
		just N and e. N must be unique (I'm not sure how this is enforced?)
- message encryption 
	- convert the message into digits. This numerfied text is M.
	- The text is then encrypted into C, via the following formula C = M^e (mod N) or C = M**e % N in python 
	- C should be a ridiculous number
- message decryption
	- The decryption formula is M = C^d(mod N)

# Progress:
[x] MVP basic implementation. 
[] more complex messages
[] encode decode over the network
