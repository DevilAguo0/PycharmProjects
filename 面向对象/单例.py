class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


mucic1 = MusicPlayer()
print(mucic1)
music2 = MusicPlayer()
print(music2)
