def format_percent(change):
    if change > 0:
        return f"+{change:.2f}%"
    else:
        return f"{change:.2f}%"

def format_price(price):
    if price >= 1.0:
        return f"${price:.2f}"
    elif price >= 0.01:
        return f"${price:.4f}"
    else:
        return f"${price:.8f}"