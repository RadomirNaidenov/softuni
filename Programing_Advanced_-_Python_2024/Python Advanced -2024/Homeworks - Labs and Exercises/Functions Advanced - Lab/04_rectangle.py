def rectangle(lenght, width):
    if not isinstance(lenght, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return  lenght * width
        

    def perimeter():
        return 2 * (lenght + width)

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

