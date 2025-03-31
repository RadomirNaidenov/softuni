def fill_the_box(height, length, width, *args):
    cube_size = height * length * width
    for arg in args:
        if arg == "Finish":
            break
        cube_size -= arg
    if cube_size <= 0:
        return f"No more free space! You have {abs(cube_size)} more cubes."
    return f"There is free space in the box. You could put {cube_size} more cubes."

