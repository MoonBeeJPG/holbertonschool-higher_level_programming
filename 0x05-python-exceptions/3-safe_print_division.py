#!/usr/bin/python3
def safe_print_division(a, b):
    qtient = None
    try:
        qtient = a / b
    except Exception:
        pass
    finally:
        if qtient is not None:
            print("Inside result: {:.1f}".format(qtient))
        else:
            print("Inside result: None")
    return qtient
