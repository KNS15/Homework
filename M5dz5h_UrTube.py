import time
import hashlib
import uuid


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        salt = uuid.uuid4().hex
        self.password = hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt
        self.age = age

    def __repr__(self):
        return f'{self.nickname}, {self.password}, {self.age}'

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if nickname in user.nickname:
                print(f'Пользователь {nickname} уже существует')
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_in(user.nickname, user.password)
            print(f'Пользователь {nickname} ({age}лет) зарегистрирован\n{nickname} Вход выполнен\n')

    def log_in(self, login: str, password: str):
        for user in self.users:
            if user.nickname == login and user.password == password:
                self.current_user = user
                break
            else:
                print('Ошибка!\nНеверный логин или пароль\n')

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for new_video in videos:
            self.videos.append(new_video)
        print(*videos, sep='\n')

    def get_videos(self, word: str):
        list_of_videos = []
        for video in self.videos:
            if word.upper() in video.title.upper():
                list_of_videos.append(video.title)
        return f', '.join(map(str, list_of_videos))

    def watch_video(self, video_for_watch: str):
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу\n')
        elif self.current_user:
            for video in self.videos:
                if video_for_watch in video.title:
                    print('Воспроизведение видео: ', video_for_watch)
                    for sec in range(1, video.duration + 1):
                        print(sec, end=' =>> ')
                        time.sleep(1)
                    print('\nКонец видео\n')
                    break
            if video_for_watch not in self.videos:
                print('Такого видео не существует')

        else:
            print('Войдите в аккаунт, или зарегистрируйтесь, чтобы посмотреть видео\n')

    def __str__(self):
        return self.videos


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)


    ur.add(v1, v2)


    print(ur.get_videos('лучший'))

    print(ur.get_videos('ПРОГ'))


    ur.watch_video('Лучший язык программирования 2024 года')

    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')


    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)


    ur.watch_video('Лучший язык программирования 2024 года!')

    print(f'\n{ur.current_user.nickname}, пароль в хэшированном виде: {ur.current_user.password}')