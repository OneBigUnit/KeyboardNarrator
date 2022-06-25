import pathlib
import playsound
import os


class Sound:
    def __init__(self, sound_path: str) -> None:
        self.relative_file_path = sound_path.replace("/", "\\")
        self.absolute_file_path = rf"{os.path.dirname(__file__)}/{self.relative_file_path}".replace("/", "\\")

    def play(self, from_path: str = "") -> None:
        try:
            if self.relative_file_path not in [str(file) for file in pathlib.Path(from_path).glob("**/*.mp3")]:
                raise ValueError() from None
            playsound.playsound(str(self), False)
        except playsound.PlaysoundException:
            raise ValueError("Audio file not found") from None

    def __str__(self) -> str:
        return self.absolute_file_path
