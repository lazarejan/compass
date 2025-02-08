def calculation(deg):
    if deg > 360:
        deg = deg % 360
    dirs = ("N", "NE", "E", "SE", "S", "SW", "W", "NW", "N")
    upd_deg = deg // 90
    real_deg = deg % 90

    if real_deg < 20:
        targ = dirs[upd_deg + upd_deg]
    elif real_deg < 70:
        targ = dirs[upd_deg + 1+ upd_deg]
    else:
        targ = dirs[upd_deg + 2+ upd_deg]
    return targ

def comp():
    while True:
        try:
            deg = int(input("enter degree you are at: "))
        except ValueError:
            print("pleas enter a number")
        else:
            break
    return calculation(deg)

def consumer_ret():
    return f"you are looking at the direction of {comp()}°"
print(consumer_ret())