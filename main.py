f = open("txt.txt")
s = f.readline()
#print(s)
for i in range(len(s)):
    if s[i] == "r" and s[i+1] == " ":
        p = 0
        while (s[i-p] != " "):
            p += 1
        while (p >= 0):
            print(s[i-p],end = '')
            p -= 1
        print(end = '\n')
