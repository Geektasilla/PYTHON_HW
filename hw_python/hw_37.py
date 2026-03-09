# 1. Воспроизведение мультимедиа
# Создайте два класса:
# AudioFileMixin — требует наличие поля audio_tracks (список треков).
# Метод play_audio() выводит:
# Воспроизведение аудио для <НазваниеКласса>:
# <название трека>
# <название трека>
from openai import videos


# VideoFileMixin — требует наличие поля video_files (список видео).
# Метод play_video() выводит:
# Воспроизведение видео для <НазваниеКласса>:
# <название видео>
# <название видео>
# Если нужное поле отсутствует — выбрасывайте AttributeError.

# Создаю Mixin класс чтобы потом примешать ее функционал к основному классу:
class AudioFileMixin:
    # Создаю метод:
    def play_audio(self):
        # Выполняю проверку на наличие атрибута
        if not hasattr(self, 'audio_tracks'):
            # Если нет, то вывожу ошибку
            raise AttributeError("Object need an'audio_tracks' attribute")
        # Воспроизведение аудио для <НазваниеКласса>:
        print(f"Play audio for {self.__class__.__name__}:")
        # печатаем <название трека>
        for track in self.audio_tracks:
            print(f"\t{track}")

# Аналогично предыдущему блоку выполняю следующий
class VideoFileMixin:
    def play_video(self):
        if not hasattr(self, 'video_files'):
            raise AttributeError("Object need a 'video_files' attribute")
        print(f'Play video for {self.__class__.__name__}: ')
        for video in self.video_files:
            print(f'\t{video}')

# 2.Устройства
# Создайте два класса:
# MediaPlayer — поддерживает только аудио. Принимает список треков.
# Laptop — поддерживает аудио и видео. Принимает списки треков и видео.
# Проверьте работу классов, вызвав методы воспроизведения.
# Данные:
# tracks = ["track1.mp3", "track2.mp3"]
# movies = ["movie.mp4", "trailer.mov"]

# Пример вывода:
# Воспроизведение аудио для MediaPlayer:
# track1.mp3
# track2.mp3
# Воспроизведение аудио для Laptop:
# track1.mp3
# track2.mp3
# Воспроизведение видео для Laptop:
# movie.mp4
# trailer.mov

# Создаю основной MediaPlayer класс и добавляю в него наследование функционала от класса AudioFileMixin:
class MediaPlayer(AudioFileMixin):
    #  инициализирую атрибуты:
    def __init__(self, audio_tracks):
        # создаю поле
        self.audio_tracks = audio_tracks

# Создаю основной Laptop класс и добавляю в него наследование функционала от класса AudioFileMixin и VideoFileMixin:
class Laptop(AudioFileMixin, VideoFileMixin):
    #  инициализирую атрибуты:
    def __init__(self, audio_tracks, video_files):
        # создаю поля
        self.audio_tracks = audio_tracks
        self.video_files = video_files

# Списки для проверки.
tracks = ['audio.mp3', 'audio.flac', 'audio.wav']
movies = ['movie.dvd', 'movie.mkv', 'movie.avi']
# Вызываю методы воспроизведения.
media_player = MediaPlayer(tracks)
media_player.play_audio()
print()

laptop = Laptop(tracks, movies)
laptop.play_audio()
laptop.play_video()
print()






