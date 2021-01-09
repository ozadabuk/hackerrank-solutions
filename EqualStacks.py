
def equalStacks(h1, h2, h3):
    while sum(h1) != sum(h2) != sum(h3):
        lists = [h1, h2, h3]
        sums = [sum(h1), sum(h2), sum(h3)]
        highest = sums.index(max(sums))
        lists[highest].pop(0)

    return sum(h1)


if __name__ == "__main__":

    result = equalStacks(h1, h2, h3)