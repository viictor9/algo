def rodCutting(length, prices):
    max_revenue = [0] * (length + 1)

    for i in range(1, length + 1):
        for j in range(i):
            max_revenue[i] = max(max_revenue[i], prices[j] + max_revenue[i - j - 1])

    return max_revenue[length]

length = int(input("Enter the length of the rod: "))
prices = list(map(int, input("Enter the prices separated by space: ").split()))

while len(prices) < length:
    print("Enter all prices equal to the length of the rod.")
    prices = list(map(int, input("Enter the prices again: ").split()))

max_revenue = rodCutting(length, prices)
print(f"Maximum profit is {max_revenue}")
