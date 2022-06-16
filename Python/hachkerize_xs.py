def decode(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    hackerized = 'Λß↻Ð☰∲ç╫¡¿├↑ღ∏☐þ¶┏§⊥üƴ₪✕¥ᶾ'
    
    ans = ''
    for c in s:
        try:
            ans += alphabet[hackerized.index(c)]
        except ValueError:
            ans += c
    
    return ans

if __name__ == "__main__":
    print("Decoded string:", decode(input("Encoded string: ")))
