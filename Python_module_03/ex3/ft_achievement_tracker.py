print("=== Achievement Tracker System ===\n")

alice_achievements = {
    "first_kill",
    "level_10",
    "treasure_hunter",
    "speed_demon",
    "treasure_hunter",
}
bob_achievements = {"first_kill", "level_10", "boss_slayer", "boss_slayer", "collector"}
charlie_achievements = {
    "level_10",
    "treasure_hunter",
    "boss_slayer",
    "speed_demon",
    "perfectionist",
}
print(f"Player alice achievements: {alice_achievements}")
print(f"Player bob achievements: {bob_achievements}")
print(f"Player charlie achievements: {charlie_achievements}")

print("\n=== Achievement Analytics ===")
unique_achievements = alice_achievements.union(bob_achievements, charlie_achievements)
print(f"All unique achievements: {unique_achievements}")
print(f"Total unique achievements: {len(unique_achievements)}")

print(
    f"\nCommon to all players: {alice_achievements.intersection(bob_achievements, charlie_achievements)}"
)

alice_only = alice_achievements.difference(bob_achievements, charlie_achievements)
bob_only = bob_achievements.difference(alice_achievements, charlie_achievements)
charlie_only = charlie_achievements.difference(alice_achievements, bob_achievements)

print(f"Rare achievements (1 player): {alice_only.union(bob_only, charlie_only)}")

print(f"\nAlice vs Bob common: {bob_achievements.intersection(alice_achievements)}")
print(f"Alice unique: {alice_achievements.difference(bob_achievements)}")
print(f"Bob unique: {bob_achievements.difference(alice_achievements)}")
