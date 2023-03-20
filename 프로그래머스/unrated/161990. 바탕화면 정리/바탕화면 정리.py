def solution(wallpaper):
    wallpaper_t = list(zip(*wallpaper))

    lux = len(wallpaper)
    luy = len(wallpaper_t)
    rdx = 0
    rdy = 0

    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            lux = i if lux > i else lux
            rdx = i + 1 if rdx < i + 1 else rdx

    for i in range(len(wallpaper_t)):
        if '#' in wallpaper_t[i]:
            luy = i if luy > i else luy
            rdy = i + 1 if rdy < i + 1 else rdy
        
    return [lux, luy, rdx, rdy]