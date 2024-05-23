
def find_h(k):
    return f"Имеем: k\nИщем: h = {-k} ед."


def find_k(h):
    return f"Имеем: h\nИщем: k = {-h} ед."


def pump(*funcs):
    def wrapper(h=0, k=0):
        for func in funcs:
            if "centrifugal" in func.__name__:
                print("Тип насоса: центробежный")
                print(find_h(func(h, k)))
            else:
                print("Тип насоса: плунжерный")
                print(find_k(func(h, k)))
            print()
    return wrapper


@pump
def centrifugal_pump(h=0, k=0):
    return h if h else k


@pump
def plower_pump(h=0, k=0):
    return h if h else k


centrifugal_pump(k=5)
plower_pump(h=25)
