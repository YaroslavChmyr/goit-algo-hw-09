import timeit

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        while amount >= coin:
            result[coin] = result.get(coin, 0) + 1
            amount -= coin
    return result


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = {coin: 0 for coin in coins}

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    res = {}
    while amount > 0:
        res[coin_used[amount]] = res.get(coin_used[amount], 0) + 1
        amount -= coin_used[amount]

    return res


amount = 123432
print(find_coins_greedy(amount))
print(find_min_coins(amount))

# Вимірюємо час виконання жадібного алгоритму
greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=100)

# Вимірюємо час виконання алгоритму динамічного програмування
dp_time = timeit.timeit(lambda: find_min_coins(amount), number=100)

# Виводимо результати порівняння
print("Час виконання жадібного алгоритму:", greedy_time)
print("Час виконання алгоритму динамічного програмування:", dp_time)