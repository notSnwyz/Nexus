from enum import Enum
import datetime


class AnimeStatus(Enum):
    PLANNING = "Planning"
    WATCHING = "Watching"
    REWATCHING = "Rewatching"
    PAUSED = "Paused"
    DROPPED = "Dropped"
    COMPLETED = "Completed"


class Anime:
    def __init__(
            self,
            name: str,
            status: AnimeStatus,
            episode_progress: int,
            total_episodes: int,
            start_date: datetime.date | None,
            end_date: datetime.date | None,
            rating: int | None
            ):

        self.name = name

        if not isinstance(status, AnimeStatus):
            raise ValueError("Invalid status")

        self.status = status

        if total_episodes <= 0:
            raise ValueError("Total episodes must be greater than 0")

        self.total_episodes = total_episodes

        if episode_progress < 0 or episode_progress > total_episodes:
            raise ValueError(
                "Episode progress must be a positive number or not be greater than total episodes"
            )

        self.episode_progress = episode_progress

        if start_date is not None and not isinstance(start_date, datetime.date):
            raise ValueError("Invalid start date")

        self.start_date = start_date

        if end_date is not None and not isinstance(end_date, datetime.date):
            raise ValueError("Invalid end date")

        if start_date is not None and end_date is not None and end_date < start_date:
            raise ValueError("End date cannot be before start date")

        self.end_date = end_date

        if (rating is not None) and ((rating < 0) or (rating > 100)):
            raise ValueError("Rating must be a number between 0 and 100")

        self.rating = rating  # Rating out of 100


anime1 = Anime(
    "NGE",
    AnimeStatus.PLANNING,
    0,
    25,
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


anime2 = Anime(
    "Ditf",
    AnimeStatus.WATCHING,
    5,
    24,
    datetime.date.today(),
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