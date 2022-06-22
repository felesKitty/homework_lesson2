words = input('Enter some words with spaces: ').split()

for w1, wx in enumerate(words, 1):
    print(f'{w1}. {wx:10}')