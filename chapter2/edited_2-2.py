from decimal import Decimal
currency = '$'
price = Decimal(24.95)
discount = Decimal(24.95 * 40 / 100)
shipping = Decimal(3 + 0.75 * 59)
total_cost = (price - discount) * 60 + shipping
print('The total wholesale cost for 60 copies is', \
      currency + str(Decimal(total_cost).quantize(Decimal('1.00'))))
