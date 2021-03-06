from sha import sha
class sha256(sha):
	word_length = 32

	# CONSTANTS

	K = [
			0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
			0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
			0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
			0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
			0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
			0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
			0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
			0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
		]

	H = [
			0x6a09e667,
			0xbb67ae85,
			0x3c6ef372,
			0xa54ff53a,
			0x510e527f,
			0x9b05688c,
			0x1f83d9ab,
			0x5be0cd19,
		]


	# FUNCS

	def S0(self, x):
		return self.rotr(x, 2) ^ self.rotr(x, 13) ^ self.rotr(x, 22)

	def S1(self, x):
		return self.rotr(x, 6) ^ self.rotr(x, 11) ^ self.rotr(x, 25)

	def g0(self, x):
		return self.rotr(x, 7) ^ self.rotr(x, 18) ^ self.shr(x, 3)

	def g1(self, x):
		return self.rotr(x, 17) ^ self.rotr(x, 19) ^ self.shr(x, 10)

	# DIGESTION

	def digest(self, p):
		m = self.parse(self.pad(p), 512)
		for b in m:
			W = self.parse(b, 32)
			for t in range(16, 64):
				x = self.g1(W[t-2]) + W[t-7] + self.g0(W[t-15]) + W[t-16]
				W.append(x & self.mask)
			
			a, b, c, d, e, f, g, h = self.H
			for t in range(64):
				T1 = (h + self.S1(e) + self.ch(e, f, g) + self.K[t] + W[t])
				T2 = (self.S0(a) + self.maj(a, b, c))
				a, b, c, d, e, f, g, h = (T1 + T2) & self.mask, a, b, c, (d + T1) & self.mask, e, f, g
			
			n = [a, b, c, d, e, f, g, h]
			for t in range(len(self.H)):
				self.H[t] += n[t]
				self.H[t] &= self.mask
		
		d = sum(c << 32*(len(self.H)-i-1) for i, c in enumerate(self.H))
		return d

s = sha256()
x = """What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."""
print(hex(s(x)))