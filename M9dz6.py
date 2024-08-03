def all_variants(text):
    i = 1
    while i <= len(text):
        x = 0
        while x + i <= len(text):
            yield text[x:x+ i]
            x += 1
        if i >= len(text):
            break
        i += 1


a = all_variants("abc")
for i in a:
    print(i)
