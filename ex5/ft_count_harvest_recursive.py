def ft_count_harvest_recursive(current=1, total=0):
    if total == 0:
        total = int(input("Days until harvest: "))
    if current > total:
        print("Harvest time!")
        return
    print("Day", current)
    ft_count_harvest_recursive(current + 1, total)
