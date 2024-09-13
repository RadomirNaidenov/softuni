def even_odd(*args):
    args = list(args)
    some_command = args.pop()
    if some_command == "even":
        return list(filter(lambda x: x % 2 == 0, args))
    elif some_command == "odd":
        return list(filter(lambda x: x % 2 != 0, args))


