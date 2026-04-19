import unicodedata

def harf_turi(belgi):
    return unicodedata.category(belgi)

# Misol:
print(harf_turi('A'))  # Lu
print(harf_turi('0'))  # Nd
print(harf_turi('a'))  # Ll
