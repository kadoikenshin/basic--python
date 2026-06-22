text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# 記号を削除する
words = text.replace(",", "").replace(".", "").split()

# 各要素の文字数を得る
lengths = list(map(len, words))

# 数値を連結
pi_digits = ''.join(map(str, lengths))

print(pi_digits)
