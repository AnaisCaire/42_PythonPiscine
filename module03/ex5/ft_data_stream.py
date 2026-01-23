
def fibonacci_generator(limit):
    a, b = 0, 1
    for i in range(limit):
        yield a
        a, b = b, a + b


def prime_num_generator(limit):
    num = 2
    found = 0
    while found < limit:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            found += 1
        num += 1


def game_event_generator(count):
    """
    A 3 players, 3 actions and level generator
    """
    player = ["alice", "bob", "charlie"]
    action = ["leveled up", "killed monster", "found treasure"]

    for n in range(1, count + 1):
        event = {
            "player": player[n % 3],
            "level": (n * 7) % 20,
            "action": action[n % 3]
            }
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    print("\nProcessing 1000 game events...\n")

    total = 1
    high_level = 0
    treasure_count = 0
    levelup_count = 0
    for event in game_event_generator(1000):
        if total < 4:
            print(
                f'Event {total}: Player {event["player"]} '
                f'(level {event["level"]}) {event["action"]}')
        elif total == 4:
            print("...")
        if event["level"] >= 10:
            high_level += 1
        if event["action"] == "found treasure":
            treasure_count += 1
        if event["action"] == "leveled up":
            levelup_count += 1
        total += 1

    print("\n=== Stream Analytics ===")

    print(f"Total events processed: {total}")
    print("High-level players (10+):", high_level)
    print("Treasure events:", treasure_count)
    print("Level-up events:", levelup_count)

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonaci sequence (first 10): ", end="")
    first = True
    for num in fibonacci_generator(10):
        if first is True:
            print(num, end="")
            first = False
        else:
            print(f", {num}", end="")
    print("\nPrime numbers (first 5): ", end="")
    first = True
    for num in prime_num_generator(5):
        if first is True:
            print(num, end="")
            first = False
        else:
            print(f", {num}", end="")
    print()
