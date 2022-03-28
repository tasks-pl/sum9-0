"""
поместить + (2+3), - (3-2), или ничего ( )
в промежутках между цифрами от 9 до 0 (в таком порядке),
чтобы в результате получилось 200.
Например: 98+76-5+43-2-10=200
"""

import itertools


def find_terms(digits, target):
    results = []

    # minus, merge with previous, plus
    signs = [-1, 0, 1]

    for digit_signs in itertools.product(*[signs] * len(digits)):
        seq_raw = [item * sign if sign != 0 else 'j' + str(item)
                   for item, sign in zip(digits, digit_signs)]

        # first digit doesn't have previous & always with plus
        if str(seq_raw[0]).startswith('j'):
            seq_raw[0] = int(str(seq_raw[0]).replace('j', ''))
        if seq_raw[0] < 0:
            seq_raw[0] *= -1

        (seq_final := []).append(seq_raw[0])
        i_src = 1
        i_trg = 1
        while i_src < len(seq_raw):
            while i_src < len(seq_raw) and \
                    (curr := str(seq_raw[i_src])).startswith('j'):
                new_prev = str(seq_final[i_trg - 1]) + curr.replace('j', '')
                seq_final[i_trg - 1] = new_prev
                i_src += 1
                if i_src >= len(seq_raw):
                    break
            if i_src >= len(seq_raw):
                break
            else:
                seq_final.append(seq_raw[i_src])
                i_src += 1
                i_trg += 1
        res = list(int(i) for i in seq_final)
        if sum(res) == target and res not in results:
            results.append(res)
    for i in sorted(results, key=len):
        print(i)


print(__doc__)
digits = [i for i in range(9, -1, -1)]
target = 200
find_terms(digits, target)
