def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""
    for cheeses_name, quantities in sorted_cheeses:
        result += f"{cheeses_name}\n"
        reversed_quanities = sorted(quantities, reverse=True)
        for quantity in reversed_quanities:
            result += f"{quantity}\n"
    
    return result



