def math_operations(*args, **kwargs):
    args = reversed(list(args))
    args = list(args)
    while args:
        for key, value in kwargs.items():
            if not args: 
                break
            if key == "a":
                kwargs[key] += args.pop()
            elif key == "s":
                kwargs[key] -= args.pop()
            elif key == "d":
                poped_arg = args.pop()
                if poped_arg == 0 or kwargs[key] == 0:
                    continue
                kwargs[key] /= poped_arg
            elif key == "m":
                kwargs[key] *= args.pop()

            
    kwargs = dict(sorted(kwargs.items(), key=lambda item: (-item[1], item[0])))
    result = []

    for key, value in kwargs.items():
        result.append(f"{key}: {value:.1f}")

    return "\n".join(result).strip()


print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))