def is_profitable(revenue, cost):
    """Return True if revenue is greater than cost."""
    return revenue > cost
 
 
def main():
    revenue = float(input("What's the revenue? "))
    cost = float(input("What's the cost? "))
    category = input("What's the product category? ").strip().lower()
 
    if is_profitable(revenue, cost):
        profit = revenue - cost
        print(f"Profit: ${profit:,.2f}")
 
        match category:
            case "electronics" | "gadget":
                print("Suggestion: Reinvest")
            case name if name.startswith("tech"):
                print("Suggestion: Reinvest")
            case "clothing" | "apparel":
                print("Suggestion: Maintain and monitor trends")
            case "food" | "grocery":
                print("Suggestion: Focus on cutting costs")
            case _:
                print("Suggestion: Review the category before investing")
    else:
        print("Not profitable. Review costs before investing.")
 
 
main()