"""สลับตัวอักษร"""

def main():
    """ทำตัวเล็ก"""
    WORD = input()
    WORD1 = WORD[::-1]
    WORD2 = WORD1.lower()
    print(WORD2)

main()
