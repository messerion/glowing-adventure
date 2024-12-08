import itertools

def all_variants2(text):

    for i in range(1, len(text) + 1):
        combinations = itertools.combinations(text, i)
        for c in combinations:
            yield ''.join(c)


a = all_variants2('abc')
print("Комбинации для 'abc':")
for i in a:
    print(i)