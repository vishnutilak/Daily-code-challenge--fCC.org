def count_change(change):
    total = sum(change)
    doll = total//100
    cent = total%100

    return f"${doll}.{cent:02d}"
