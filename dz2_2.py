vice_versa = list(input('Enter some numbers here (without spaces!): '))

for v in range(0, len(vice_versa) - 1, 2):
    vice_versa[v + 1], vice_versa[v] = vice_versa[v], vice_versa[v + 1]

print(vice_versa)