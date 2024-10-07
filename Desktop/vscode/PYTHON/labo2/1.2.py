def totalValue(stock):
    return sum(item["quantity"] * item["price"] for item in stock.values())
