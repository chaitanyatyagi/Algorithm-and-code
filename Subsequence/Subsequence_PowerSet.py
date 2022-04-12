def subsequence():
    s = "abc"
    n = len(s)
    for num in range(2**n):
        sub = ""
        for i in range(n):
            if num & (1<<i):
                sub += s[i]
        print({sub})
subsequence()


