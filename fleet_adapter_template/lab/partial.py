from functools import partial

def calculate_discount(price, percentage, currency="USD"):
    discount = price * (percentage / 100)
    return f"Discount: {discount:.2f} {currency}"

ten_percent_usd = partial(calculate_discount, percentage=10, currency="USD")
print(ten_percent_usd(100))  # Discount: 10.00 USD
print(ten_percent_usd(50))   # Discount: 5.00 USD
