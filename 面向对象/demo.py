class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance


music1 = MusicPlayer()
music2 = MusicPlayer()
print(music1)
print(music1)
