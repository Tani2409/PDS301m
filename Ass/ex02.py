# Dữ liệu ban đầu
products = {
    "Apple": {"price": 2.0, "category": "Fruits"},
    "Milk": {"price": 3.0, "category": "Dairy"},
    "Chips": {"price": 1.0, "category": "Snacks"},
    "Carrot": {"price": 2.5, "category": "Vegetables"},
}

discounts = {
    "Fruits": 0.10,
    "Vegetables": 0.05,
    "Dairy": 0.01,
    "Snacks": 0.10
}

# Nhập ngân sách
budget = float(input("Nhập ngân sách của bạn ($): "))
remaining = budget
bought_items = []


while True:
    print("Danh sách sản phẩm hiện có:", ", ".join(products.keys()))
    choice = input("Chọn sản phẩm (hoặc nhập 'exit' để kết thúc): ").capitalize().strip()

    if choice == "Exit":
        print("\nKết thúc mua sắm.")
        break

    # Kiểm tra hợp lệ
    if choice not in products:
        print(" Sản phẩm không tồn tại. Hãy thử lại!\n")
        continue

    # Lấy thông tin sản phẩm
    info = products[choice]
    cat = info["category"]
    base_price = info["price"]
    sale = discounts.get(cat, 0)
    final_cost = base_price * (1 - sale)

    # Kiểm tra ngân sách
    if final_cost > remaining:
        print(f"Không đủ ngân sách cho {choice}. Số dư hiện tại: ${remaining:.2f}\n")
        continue

    # Mua hàng
    remaining -= final_cost
    bought_items.append((choice, cat, base_price, sale, final_cost))

    print(f" Đã mua {choice} ({cat}) với giá ${final_cost:.2f} (giảm {sale*100:.0f}%).")
    print(f" Ngân sách còn lại: ${remaining:.2f}\n")
    
# Tổng kết
total_spent = sum(item[4] for item in bought_items)
print("\n--- HÓA ĐƠN ---")
for item, cat, p, disc, f in bought_items:
    print(f"{item:<8} | {cat:<12} | Giá gốc: ${p:<4} | Giảm: {disc*100:.0f}% | Trả: ${f:.2f}")
print(f"\nTổng chi tiêu: ${total_spent:.2f}")
print(f"Số dư còn lại: ${remaining:.2f}")