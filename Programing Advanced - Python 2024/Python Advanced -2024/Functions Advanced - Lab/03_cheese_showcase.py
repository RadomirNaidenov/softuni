def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = []
    for cheeses_name, quantities in sorted_cheeses:
        result.append(cheeses_name)
        result.extend([str(quantity) for quantity in sorted(quantities, reverse=True)])
    
    return "\n".join(result)

