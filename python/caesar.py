let = 'abcdefghijklmnopqrstuvwxyz'
blet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def word_change(st, n, j):
    rt = ''
    if j == len(st) - 1 and st[len(st) - 1] not in '.?!':
        n += 1
    for k in range(j - n, j + 1):
        if st[k] in let:
            if let.index(st[k]) + n > 25:
                rt += let[let.index(st[k]) + n - 26]
            else:
                rt += let[let.index(st[k]) + n]
        
        if st[k] in blet:
            if blet.index(st[k]) + n > 25:
                rt += blet[blet.index(st[k]) + n - 26]
            else:
                rt += blet[blet.index(st[k]) + n]
    return rt


s = input()
counter = 0
result = ''
i = 0

while i < len(s):
    if s[i] not in let and s[i] not in blet:
        result += s[i]
    
    else:
        while i < len(s) - 1 and (s[i] in let or s[i] in blet):
            counter += 1
            i += 1
        result += word_change(s, counter, i)
        if s[i] in '.!? ,-"':
            result += s[i]
        counter = 0
    
    i += 1

print(result)