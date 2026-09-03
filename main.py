from models.anime import Anime, AnimeStatus

anime1 = Anime(
    "Chainsaw Man – The Movie: Reze Arc",
    AnimeStatus.PLANNING,
    0,
    1,
    None,
    None,
    None
)

print(anime1.name)
print(anime1.status.value)
print(anime1.episode_progress)
print(anime1.total_episodes)
print(anime1.start_date)
print(anime1.end_date)
print(anime1.rating)

anime1.update_progress(1)

print("\n")
print(anime1.name)
print(anime1.status.value)
print(anime1.episode_progress)
print(anime1.total_episodes)
print(anime1.start_date)
print(anime1.end_date)
print(anime1.rating)

anime2 = Anime(
    "Ditf",
    AnimeStatus.PLANNING,
    0,
    24,
    None,
    None,
    None
)

print("\n")
print(anime2.name)
print(anime2.status.value)
print(anime2.episode_progress)
print(anime2.total_episodes)
print(anime2.start_date)
print(anime2.end_date)
print(anime2.rating)

anime2.update_progress(1)

print("\n")
print(anime2.name)
print(anime2.status.value)
print(anime2.episode_progress)
print(anime2.total_episodes)
print(anime2.start_date)
print(anime2.end_date)
print(anime2.rating)

anime2.update_progress(24)

print("\n")
print(anime2.name)
print(anime2.status.value)
print(anime2.episode_progress)
print(anime2.total_episodes)
print(anime2.start_date)
print(anime2.end_date)
print(anime2.rating)