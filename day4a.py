import hashlib

crypto = 'bgvyzdsv'
fiveZeroIndex = 0
i = 0

while True:
    i += 1
    digest = hashlib.md5((crypto + str(i)).encode())
    result = digest.hexdigest()
    """
    if result[:5] == '00000':
        print(i)
        print(result)
        break
    # 254575 is correct
    """
    if result[:6] == '000000':
        print(i)
        print(result)
        break
    # correct is 1038736


"""
# -*- coding: utf-8 -*-
import hashlib

crypto = 'bgvyzdsv'
i = 0 # Reknare
fiveZeroIndex = 0

while True:
    i += 1
    hash = hashlib.md5(str(crypto).encoding='utf-8' + str(i).encoding='utf-8').hexdigest()

    if not fiveZeroIndex and hash.startswith('0' * 5):
        fiveZeroIndex = i

    # exit
    if fiveZeroIndex:
        break


# Print answer
print("The 5 zero index is: ", fiveZeroIndex)
"""