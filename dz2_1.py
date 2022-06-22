matrix = [(3, 2, 7)]
dif_elements = [6, 17.5, bin(88), (oct(87)), (hex(22)), (1 + 6j), 'string',
                [8, 'txt', 589.3, None], (1836, 11, 18), {'zebra'},
                {12: 'here', 34: 'is', 5.6: 222}, frozenset(), False,
                True, (b'whale'), bytearray(b"here is zebra"), None,
                ZeroDivisionError, zip(*matrix)]

for l, element in enumerate(dif_elements, 1):
    print(f'{l}. {element} / {type(element)}')
