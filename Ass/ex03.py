# dữ liệu gốc
items_list   = ['Apple', 'Milk', 'Chips', 'Carrot']
prices_dict  = {'Apple': 2.0, 'Milk': 3.0, 'Chips': 1.0, 'Carrot': 2.5}
category_list = ['Fruits', 'Vegatables', 'Dairy', 'Snacks']         
discount_dict = {'Fruits': 0.10, 'Vegatables': 0.05, 'Dairy': 0.07, 'Snacks': 0.10}

ITEM_TO_CATEGORY = dict(zip(items_list, category_list))

def add_item_flow(state):
    print(f"Available items: {items_list}")
    item = input("Enter your item (or quit to finish): ").strip().title()

    if item == "Quit":
        state["running"] = False
        return

    if item not in items_list:
        print("Item is not in list.")
        return

    cat = ITEM_TO_CATEGORY[item]
    print("Category of the item above is:", cat)

    price = prices_dict[item]
    disc  = discount_dict.get(cat, 0.0)
    final = price * (1 - disc)

    # kiểm tra ngân sách
    if state["budget_left"] - final < 0:
        print("Not enough budget to this item.")
        return

    # cập nhật
    state["purchases"].append((item, cat, price, disc, final))
    state["total"] += final
    state["budget_left"] -= final

    print(f"Applied {disc:.0%} discount.")
    print(f"Added {item}. Remaining budget: ${state['budget_left']:.2f}\n")

def remove_item_flow(state):
    if not state["purchases"]:
        print("No items to remove.")
        return

    print("Current purchases:")
    for i, (it, cat, p, d, f) in enumerate(state["purchases"], start=1):
        print(f"{i}. {it} - ${f:.2f}")

    item = input("Enter the number of the item to remove (or 0 to cancel): ").strip()
    try:
        idx = int(item)
    except ValueError:
        print("Please enter a valid number.")
        return

    if idx == 0:
        return
    if 1 <= idx <= len(state["purchases"]):
        it, cat, p, d, f = state["purchases"].pop(idx - 1)
        state["total"] -= f
        state["budget_left"] += f
        print(f"Removed {it}. Refunded ${f:.2f}. New budget: ${state['budget_left']:.2f}")
    else:
        print("Invalid choice.")

def view_cart_flow(state):
    if not state["purchases"]:
        print("Your cart is empty.")
        return

    print("\n============================== RECEIPT ==============================")
    header = f"{'Item':<10}{'Category':<14}{'Price':<10}{'Discount':<10}{'Final':<10}"
    print(header)
    for it, cat, p, d, f in state["purchases"]:
        print(f"{it:<10}{cat:<14}${p:<9.2f}{d:<10.0%}${f:<9.2f}")
    print("---------------------------------------------------------------------")
    print(f"TOTAL  : ${state['total']:.2f}")
    print(f"BUDGET : ${state['budget_init']:.2f}")
    print(f"LEFT   : ${state['budget_left']:.2f}")
    print("STATUS : " + ("OVER BUDGET" if state["total"] > state["budget_init"] else "UNDER BUDGET"))
    print("=====================================================================\n")

def main():
    # input ngân sách
    while True:
        try:
            init_budget = float(input("Enter your budget: $").strip())
            break
        except ValueError:
            print("Please enter a valid number.")

    # state gom lại 1 chỗ, tránh global
    state = {
        "budget_init": init_budget,
        "budget_left": init_budget,
        "purchases": [],
        "total": 0.0,
        "running": True
    }

    # vòng lặp menu
    while True:
        print("=== MENU ===")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Finish shopping")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_item_flow(state)
            if not state["running"]:
                break
        elif choice == "2":
            remove_item_flow(state)
        elif choice == "3":
            view_cart_flow(state)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for shopping!")

if __name__ == "__main__":
    main()
