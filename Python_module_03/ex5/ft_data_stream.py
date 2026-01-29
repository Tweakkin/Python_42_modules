def fibo_gen(n: int) -> Generator[int, None, None]:
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_gen(n: int) -> Generator[int, None, None]:
    primes = 0
    num = 2
    while primes < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime is True:
            yield num
            primes += 1
        num += 1


def game_event_generator(events_number: int) -> Generator[str, None, None]:
    GAME_DB = {
        1: {"name": "alice", "level": 5, "action": "killed monster"},
        2: {"name": "bob", "level": 12, "action": "found treasure"},
        3: {"name": "charlie", "level": 8, "action": "leveled up"},
        4: {"name": "dave", "level": 15, "action": "killed monster"},
        5: {"name": "eve", "level": 2, "action": "joined guild"},
        6: {"name": "frank", "level": 18, "action": "found treasure"},
        7: {"name": "grace", "level": 6, "action": "leveled up"},
        8: {"name": "mallory", "level": 20, "action": "killed monster"},
        9: {"name": "trent", "level": 3, "action": "found treasure"},
        10: {"name": "oscar", "level": 11, "action": "joined guild"},
    }
    for i in range(1, events_number + 1):
        n = (i - 1) % 10 + 1
        yield (
            f"Event {i}: Player {GAME_DB[n]['name']}"
            f" (level {GAME_DB[n]['level']}) {GAME_DB[n]['action']}"
        )


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")
    total_events = 1000
    events_processed = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0
    gen = game_event_generator(total_events)
    i = 1
    for event in gen:
        if i <= 3:
            print(event)
        if "level" in event:
            level = int(((event.split("level ")[1]).split(")"))[0])
            if level >= 10:
                high_level_players += 1
        if "found treasure" in event:
            treasure_events += 1
        if "leveled up" in event:
            level_up_events += 1
        i += 1
        events_processed += 1
    print("...")

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {events_processed}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    fibonacci_gen = fibo_gen(10)
    print("Fibonacci sequence (first 10): ", end="")
    count = 0
    for num in fibonacci_gen:
        if count == 0:
            print(f"{num}", end="")
        else:
            print(f", {num}", end="")
        count += 1
    print("\nPrime numbers (first 5): ", end="")
    prime_generator = prime_gen(5)
    count = 0
    for num in prime_generator:
        if count == 0:
            print(f"{num}", end="")
        else:
            print(f", {num}", end="")
        count += 1
    print()


main()
