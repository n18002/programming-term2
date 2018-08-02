TAX_RATE = 8
rate = [13600, 14500, 16000, 1111, 11677]
print(list(map(lambda x: round(x * (1 + TAX_RATE / 100), -1), rate)))
