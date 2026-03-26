print("=== Achievement Tracker System ===\n")

alice = {
    "first_kill",
    "level_10",
    "treasure_hunter",
    "speed_demon",
    "treasure_hunter",
}
bob = {"first_kill", "level_10", "boss_slayer", "boss_slayer", "collector"}
charlie = {
    "level_10",
    "treasure_hunter",
    "boss_slayer",
    "speed_demon",
    "perfectionist",
}
print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

print("\n=== Achievement Analytics ===")
unique = alice.union(bob, charlie)
print(f"All unique achievements: {unique}")
print(f"Total unique achievements: {len(unique)}")

print(
    f"\nCommon to all players: {alice.intersection(bob, charlie)}"
)

alice_only = alice.difference(bob, charlie)
bob_only = bob.difference(alice, charlie)
charlie_only = charlie.difference(alice, bob)

print(f"Rare achievements (1 player): "
      f"{alice_only.union(bob_only, charlie_only)}")

print(f"\nAlice vs Bob common: {bob.intersection(alice)}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")
