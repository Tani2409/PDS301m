# ---- function 1: tao danh muc dau tu tu list ----
def create_portfolio(symbols, prices):
    """tao danh muc dau tu tu 2 list ma va gia"""
    portfolio = []
    for i in range(len(symbols)):
        portfolio.append({"symbol": symbols[i], "price": prices[i]})
    return portfolio


# ---- function 2: tinh tong gTri danh muc ----
def total_portfolio_value(portfolio, quantities):
    """tinh tong gTri danh muc dua tren gia va so luong"""
    total_gTri = 0
    for i, stock in enumerate(portfolio):
        total_gTri += stock["price"] * quantities[i]
    return round(total_gTri, 2)


# ---- function 3: tim ma trung lap (dung set) ----
def find_duplicates(symbols):
    """kiem tra xem danh sach ma co phieu co bi trung khong"""
    duplicates = set([s for s in symbols if symbols.count(s) > 1])
    return duplicates if duplicates else "khong co ma trung"


# ---- function 4: chuyen danh muc sang dang tuple ----
def portfolio_to_tuples(portfolio):
    """chuyen danh sach co phieu sang list tuple (symbol, price)"""
    return [(stock["symbol"], stock["price"]) for stock in portfolio]


# ---- function 5: tinh do bien dong trung binh hang ngay ----
def average_daily_volatility(prices):
    """tinh % bien dong trung binh giua cac ngay lien tiep"""
    if len(prices) < 2:
        return 0.0
    changes = []
    for i in range(1, len(prices)):
        change = abs((prices[i] - prices[i-1]) / prices[i-1] * 100)
        changes.append(change)
    avg_volatility = sum(changes) / len(changes)
    return round(avg_volatility, 2)


# ---- demo (gom 1 khoi) ----
if __name__ == "__main__":
    print("--- demo phase 2 - portfolio utilities ---")

    # demo 1: volatility
    prices_demo_vol = [100, 103, 97, 101, 105, 98, 102]
    vol = average_daily_volatility(prices_demo_vol)
    print(f"bien dong trung binh hang ngay: {vol}%")

    # demo 2: portfolio utils
    symbols = ["fpt", "vcb", "mbb", "vic", "fpt"]
    prices = [95.5, 89.2, 23.1, 60.8, 95.5]
    quantities = [10, 5, 20, 8, 10]

    # 1. list + dict - tao danh muc dau tu
    portfolio = create_portfolio(symbols, prices)
    print("\n1. danh muc dau tu:")
    for stock in portfolio:
        print(stock)

    # 2. tinh tong gTri danh muc
    total_gTri = total_portfolio_value(portfolio, quantities)
    print(f"\n2. tong gTri danh muc: {total_gTri} usd")

    # 3. set - kiem tra ma co phieu trung
    dup = find_duplicates(symbols)
    print(f"\n3. ma trung lap: {dup}")

    # 4. tuple - chuyen danh muc sang dang tuple
    portfolio_tuples = portfolio_to_tuples(portfolio)
    print(f"\n4. dang tuple: {portfolio_tuples}")
