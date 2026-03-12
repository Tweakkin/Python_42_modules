from .elements import create_fire, create_water, create_air, create_earth


def healing_potion():
    fire = create_fire()
    water = create_water()
    return f"Healing potion brewed with {fire} and {water}"


def strength_potion():
    fire = create_fire()
    earth = create_earth()
    return f"Strength potion brewed with {earth} and {fire}"


def invisibility_potion():
    air = create_air()
    water = create_water()
    return f"Invisibility potion brewed with {air} and {water}"


def wisdom_potion():
    air = create_air()
    earth = create_earth()
    fire = create_fire()
    water = create_water()
    return (f"Wisdom potion brewed with all elements: "
            f"{fire}, {water}, "
            f"{earth}, {air}"
            )
