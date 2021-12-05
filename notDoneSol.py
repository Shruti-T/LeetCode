# -------------------------------------- Q17) reverse bits -----------------------------------------------------
# Reverse bits of a given 32 bits unsigned integer

# cases: 600, Runtime: 24 ms, Memory Usage: 13.3 MB

# def reverseBits(self, n):
#         result = 0
#         for i in range(32):
#             result <<= 1
#             result |= n & 1
#             n >>= 1
#         return result