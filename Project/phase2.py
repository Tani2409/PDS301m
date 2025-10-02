# ===============================
# 1) LIST — Tính chuỗi drawdown
# ===============================
def compute_drawdowns(prices):
    """
    Trả về:
      - drawdowns: list % drawdown tại từng thời điểm (âm hoặc 0)
      - max_dd:    mức drawdown lớn nhất (âm, vd: -12.3 nghĩa -12.3%)
    Yêu cầu: prices là list[float] theo thời gian (cũ -> mới).
    """
    if not prices:
        return [], 0.0

    peak = prices[0]
    drawdowns = []
    max_dd = 0.0  # số âm nhỏ nhất theo trị tuyệt đối lớn nhất

    for p in prices:
        if p > peak:
            peak = p
        dd = (p - peak) / peak * 100.0
        drawdowns.append(dd)
        if dd < max_dd:
            max_dd = dd
    return drawdowns, max_dd


# =============================================
# 2) DICT — Gộp lệnh để ra vị thế và P&L tạm tính
# =============================================
def build_portfolio_positions(trades, last_prices):
    """
    trades: list[dict] mỗi dict: {"symbol": str, "side": "BUY"/"SELL", "qty": int/float, "price": float}
    last_prices: dict {symbol: last_price}
    Trả về dict:
      {
        symbol: {
          "net_qty": ...,
          "avg_cost": ...,           # giá vốn bình quân có trọng số
          "last_price": ...,
          "market_value": ...,
          "unrealized_pnl": ...
        },
        ...
      }
    """
    positions = {}

    for t in trades:
        sym = t["symbol"]
        side = t["side"].upper()
        qty = float(t["qty"])
        price = float(t["price"])

        if sym not in positions:
            positions[sym] = {"net_qty": 0.0, "avg_cost": 0.0}

        # Cập nhật avg_cost theo phương pháp bình quân gia quyền khi tăng vị thế
        # Khi giảm vị thế (bán), avg_cost giữ nguyên cho đến khi về 0.
        if side == "BUY":
            old_qty = positions[sym]["net_qty"]
            new_qty = old_qty + qty
            if new_qty > 0:
                positions[sym]["avg_cost"] = (
                    (old_qty * positions[sym]["avg_cost"] + qty * price) / new_qty
                )
            positions[sym]["net_qty"] = new_qty
        elif side == "SELL":
            positions[sym]["net_qty"] -= qty
            # nếu về 0 thì reset avg_cost để tránh “treo” giá vốn
            if abs(positions[sym]["net_qty"]) < 1e-9:
                positions[sym]["net_qty"] = 0.0
                positions[sym]["avg_cost"] = 0.0
        else:
            raise ValueError("side phải là BUY hoặc SELL")

    # Bổ sung giá thị trường & P&L
    for sym, pos in positions.items():
        last = float(last_prices.get(sym, 0.0))
        mv = pos["net_qty"] * last
        pnl = (last - pos["avg_cost"]) * pos["net_qty"]
        pos.update({
            "last_price": last,
            "market_value": mv,
            "unrealized_pnl": pnl
        })

    return positions


# ===================================================
# 3) SET — Tìm danh mục trùng nhau giữa 2 danh sách
# ===================================================
def overlapping_holdings(portfolio_a, portfolio_b):
    """
    portfolio_a, portfolio_b: iterable các mã (có thể trùng)
    Trả về set các mã xuất hiện ở CẢ HAI danh mục (giao hai tập).
    """
    return set(portfolio_a) & set(portfolio_b)


# ==========================================
# 4) TUPLE — Tóm tắt rủi ro (mean, std-dev)
# ==========================================
def risk_summary(returns):
    """
    returns: list các % thay đổi (vd: 1.2 nghĩa +1.2%)
    Trả về tuple (mean_return, std_dev) theo %.
    - mean_return: trung bình
    - std_dev: độ lệch chuẩn mẫu (n-1)
    """
    n = len(returns)
    if n == 0:
        return (0.0, 0.0)
    mean = sum(returns) / n
    if n == 1:
        return (mean, 0.0)
    var = sum((r - mean) ** 2 for r in returns) / (n - 1)
    std = var ** 0.5
    return (mean, std)


# -------------------
# Demo nho nhỏ
# -------------------
if __name__ == "__main__":
    prices = [100, 98, 102, 97, 95, 99, 101, 103]  # ví dụ giá đóng cửa

    # 1) LIST – Drawdowns
    dds, max_dd = compute_drawdowns(prices)
    print("Drawdowns (%):", [round(x, 2) for x in dds])
    print("Max drawdown (%):", round(max_dd, 2))

    # 2) DICT – Vị thế & PnL
    trades = [
        {"symbol": "FPT", "side": "BUY",  "qty": 100, "price": 85},
        {"symbol": "FPT", "side": "BUY",  "qty": 50,  "price": 90},
        {"symbol": "VCB", "side": "BUY",  "qty": 80,  "price": 72},
        {"symbol": "FPT", "side": "SELL", "qty": 60,  "price": 92},
    ]
    last_prices = {"FPT": 91, "VCB": 74}
    positions = build_portfolio_positions(trades, last_prices)
    print("Positions:", positions)

    # 3) SET – Giao 2 danh mục
    my_port = ["FPT", "VCB", "MBB", "MWG", "FPT"]
    friend_port = ["HPG", "MWG", "VCB", "VIC", "VCB"]
    print("Overlap:", overlapping_holdings(my_port, friend_port))  # {'MWG', 'VCB'}

    # 4) TUPLE – Risk summary
    # giả lập daily returns (%)
    returns = [1.0, -2.0, 1.5, -0.5, 0.8, 0.0, 1.2]
    mean_ret, std_dev = risk_summary(returns)
    print("Risk summary (mean %, std %):", (round(mean_ret, 3), round(std_dev, 3)))
