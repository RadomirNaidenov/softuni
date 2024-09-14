def func_executor(*args):
    result = ""
    for arg in args:
        func_name = arg[0]
        tuple_elements = arg[1]
        result += f"{func_name.__name__} - {func_name(*tuple_elements)}\n"
    
    return result



