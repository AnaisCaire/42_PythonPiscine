

def AchievementHunter():
    """
    Tool to handle unique collections of acheivements
    """
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {
        'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
        'perfectionist'}

    print("=== Achievement Tracker System ===\n")

    players = [("alice", alice), ("bob", bob), ("charlie", charlie)]
    for player, ach in players:
        print(f"Player {player} achievements: {ach}")

    print("\n=== Achievement Analytics ===")
    all_unique = alice.union(bob, charlie)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")

    common = alice.intersection(bob, charlie)
    print(f"\nCommon to all players: {common}")

    only_alice = alice.difference(bob.union(charlie))
    only_bob = bob.difference(alice.union(charlie))
    only_charlie = charlie.difference(alice.union(bob))
    rare = only_alice.union(only_bob, only_charlie)
    print(f"Rare achievements (1 player): {rare}")

    alice_bob = alice.intersection(bob)
    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)
    print(f"\nAlice vs Bob common: {alice_bob}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    AchievementHunter()
