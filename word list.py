from mnemonic import Mnemonic
mnemo = Mnemonic("english")
entropy_bits = 128  # 12 words
mnemonic_phrase = mnemo.generate(strength=entropy_bits)
print(mnemonic_phrase)
