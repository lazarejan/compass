def calculation(deg):
    if deg > 360:
        deg = deg % 360
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    upd_deg = deg // 45
    if deg % 45 >= 20:
        targ = dirs[upd_deg + 1] + "°"
    else:
        targ = dirs[upd_deg] + "°"
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