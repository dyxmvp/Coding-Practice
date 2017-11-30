def delete_nth(order,max_e):
    # code here
    e_list = []
    for o in order:
        if e_list.count(o) < max_e:
            e_list.append(o)
    return e_list