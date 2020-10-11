def sol(stocks):
    min_stock = 1e9
    for stock in stocks:
        min_stock = min(min_stock, int(stock))
        if int(stock) > min_stock:
            profit = int(stock) - min_stock
    else:
        return 0

    return profit


if __name__ == "__main__":
    stocks = list(input().split())
    print(sol(stocks))
