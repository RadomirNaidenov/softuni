def grocery_store(**kwargs):
    result = ""
    for product, quantity in\
        sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0])):
        result += f"{product}: {quantity}\n"
    
    return result



