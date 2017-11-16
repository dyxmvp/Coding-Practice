def race(v1, v2, g):
    v_diff = v2 - v1
    if v_diff <= 0:
        return None
    else:
        t = g / v_diff
        t_h = int(t)
        t_min = int(round((t - t_h) * 60, 10))
        t_s = int(((t - t_h) * 60 - t_min) * 60)
        return [t_h, t_min, t_s]