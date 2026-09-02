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
            raise ValueError("Episode progress cannot be negative or greater than total episodes")

        self.episode_progress = episode_progress

        if start_date is not None and not isinstance(start_date, datetime.date):
            raise ValueError("Invalid start date")

        self.start_date = start_date

        if end_date is not None and not isinstance(end_date, datetime.date):
            raise ValueError("Invalid end date")

        if start_date is not None and end_date is not None and end_date < start_date:
            raise ValueError("End date cannot be before start date")

        self.end_date = end_date

        if rating is not None and (rating < 0 or rating > 100):
            raise ValueError("Rating must be a number between 0 and 100")

        self.rating = rating  # Rating out of 100


    def update_progress(
            self,
            new_progress: int
            ):
        
        if new_progress < 0 or new_progress > self.total_episodes:
            raise ValueError("Episode progress cannot be negative or greater than total episodes")

        self.episode_progress = new_progress

    def change_status(
            self,
            new_status: AnimeStatus
            ):

        if not isinstance(new_status, AnimeStatus):
            raise ValueError("Invalid status")

        if new_status == AnimeStatus.COMPLETED and self.end_date is None:
            self.end_date = datetime.date.today()

        self.status = new_status