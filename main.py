# 1
royxat = ["hello", "say", "hi", "welcome"]

natija = list(map(lambda w: f"{w[0]}-{len(w)}", royxat))
print(natija)


# 2
royxat = ["Ali Valiyev", "Bobur Yo'ldoyev", "Stive Jobs", "Bill Gates"]

natija = list(map(lambda x: x.split()[0] + " " + x.split()[1][0] + ".", royxat))
print(natija)


# 3
royxat = ["Ali", "Bobur", "Stive", "Santyago"]

natija = list(map(lambda w: w + str(len(w)), royxat))
print(natija)


# 4
sozlar = ["HELLo", "saY", "hi", "Welcome"]

natija = list(map(lambda w: w[:-1] + w[-1].upper(), sozlar))
print(natija)

