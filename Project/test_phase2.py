# test_core_finance_ds.py
import math
import pytest

from phase2 import (
    compute_drawdowns,
    build_portfolio_positions,
    overlapping_holdings,
    risk_summary,
)

# -----------------------------
# Tests for compute_drawdowns()
# -----------------------------
def test_compute_drawdowns_basic():
    prices = [100, 98, 102, 97, 95, 99, 101, 103]
    dds, max_dd = compute_drawdowns(prices)

    # độ dài khớp
    assert len(dds) == len(prices)

    # drawdown tại đỉnh phải = 0, sau đó âm
    assert pytest.approx(dds[0], 1e-9) == 0.0
    # sau khi đạt đỉnh mới 102, drawdown ở đó phải 0
    assert any(abs(x) < 1e-9 for x in dds[:3])  # ở index 2 phải ~0

    # max drawdown là số âm nhỏ nhất (lỗ nhiều nhất)
    assert max_dd <= 0.0
    # chuỗi chứa một số âm (do có giảm từ đỉnh)
    assert any(x < 0 for x in dds)

def test_compute_drawdowns_empty():
    dds, max_dd = compute_drawdowns([])
    assert dds == []
    assert max_dd == 0.0

def test_compute_drawdowns_monotonic_up():
    prices = [10, 11, 12, 13]
    dds, max_dd = compute_drawdowns(prices)
    # luôn ở đỉnh mới → drawdown luôn 0
    assert all(pytest.approx(x, 1e-9) == 0.0 for x in dds)
    assert pytest.approx(max_dd, 1e-9) == 0.0

def test_compute_drawdowns_monotonic_down():
    prices = [10, 9, 8, 7]
    dds, max_dd = compute_drawdowns(prices)
    # drawdown giảm dần, max_dd là phần tử cuối (âm nhất)
    assert dds[0] == 0.0
    assert dds[-1] < dds[1] < 0
    assert max_dd == min(dds)


# -----------------------------------
# Tests for build_portfolio_positions()
# -----------------------------------
def test_build_portfolio_positions_basic():
    trades = [
        {"symbol": "FPT", "side": "BUY",  "qty": 100, "price": 85},
        {"symbol": "FPT", "side": "BUY",  "qty": 50,  "price": 90},
        {"symbol": "VCB", "side": "BUY",  "qty": 80,  "price": 72},
        {"symbol": "FPT", "side": "SELL", "qty": 60,  "price": 92},
    ]
    last_prices = {"FPT": 91, "VCB": 74}
    pos = build_portfolio_positions(trades, last_prices)

    # tồn tại 2 symbol
    assert set(pos.keys()) == {"FPT", "VCB"}

    # FPT: net_qty = 100 + 50 - 60 = 90
    assert pytest.approx(pos["FPT"]["net_qty"], 1e-9) == 90.0

    # avg_cost sau 2 lệnh BUY: (100*85 + 50*90)/150 = 86.666...
    assert pytest.approx(pos["FPT"]["avg_cost"], 1e-9) == (100*85 + 50*90) / 150

    # last_price lấy từ dict
    assert pos["FPT"]["last_price"] == 91

    # market_value = net_qty * last_price
    assert pytest.approx(pos["FPT"]["market_value"], 1e-9) == 90.0 * 91

    # unrealized_pnl = (last - avg_cost) * net_qty
    expected_pnl_fpt = (91 - pos["FPT"]["avg_cost"]) * 90.0
    assert pytest.approx(pos["FPT"]["unrealized_pnl"], 1e-9) == expected_pnl_fpt

    # VCB: chỉ BUY 80 @72, last 74
    assert pytest.approx(pos["VCB"]["net_qty"], 1e-9) == 80.0
    assert pytest.approx(pos["VCB"]["avg_cost"], 1e-9) == 72.0
    assert pos["VCB"]["last_price"] == 74
    assert pytest.approx(pos["VCB"]["market_value"], 1e-9) == 80.0 * 74.0
    assert pytest.approx(pos["VCB"]["unrealized_pnl"], 1e-9) == (74 - 72) * 80.0

def test_build_portfolio_positions_round_trip_to_zero():
    trades = [
        {"symbol": "MBB", "side": "BUY",  "qty": 10, "price": 20},
        {"symbol": "MBB", "side": "SELL", "qty": 10, "price": 21},
        {"symbol": "MBB", "side": "BUY",  "qty": 5,  "price": 22},
    ]
    last_prices = {"MBB": 23}
    pos = build_portfolio_positions(trades, last_prices)

    # Sau khi về 0, avg_cost reset về 0 rồi mua mới 5 @22 => net_qty=5, avg_cost=22
    assert pytest.approx(pos["MBB"]["net_qty"], 1e-9) == 5.0
    assert pytest.approx(pos["MBB"]["avg_cost"], 1e-9) == 22.0
    assert pos["MBB"]["last_price"] == 23
    assert pytest.approx(pos["MBB"]["unrealized_pnl"], 1e-9) == (23 - 22) * 5.0

def test_build_portfolio_positions_invalid_side():
    trades = [{"symbol": "ABC", "side": "HOLD", "qty": 1, "price": 1.0}]
    with pytest.raises(ValueError):
        build_portfolio_positions(trades, {"ABC": 1.0})


# --------------------------------
# Tests for overlapping_holdings()
# --------------------------------
def test_overlapping_holdings_basic():
    a = ["FPT", "VCB", "MBB", "MWG", "FPT"]
    b = ["HPG", "MWG", "VCB", "VIC", "VCB"]
    overlap = overlapping_holdings(a, b)
    assert overlap == {"MWG", "VCB"}

def test_overlapping_holdings_no_overlap():
    a = ["AAA", "BBB"]
    b = ["CCC", "DDD"]
    assert overlapping_holdings(a, b) == set()


# -------------------------
# Tests for risk_summary()
# -------------------------
def test_risk_summary_basic():
    returns = [1.0, -2.0, 1.5, -0.5, 0.8, 0.0, 1.2]
    mean_ret, std = risk_summary(returns)

    # mean kiểm tra gần đúng
    assert pytest.approx(mean_ret, 1e-9) == sum(returns)/len(returns)

    # std-dev mẫu: sqrt( sum((x-mean)^2)/(n-1) )
    mean = sum(returns)/len(returns)
    var = sum((r - mean)**2 for r in returns) / (len(returns)-1)
    expected_std = math.sqrt(var)
    assert pytest.approx(std, 1e-9) == expected_std

def test_risk_summary_edge_cases():
    # empty
    mean_ret, std = risk_summary([])
    assert mean_ret == 0.0 and std == 0.0

    # single value → std = 0
    mean_ret, std = risk_summary([2.5])
    assert mean_ret == 2.5 and std == 0.0
