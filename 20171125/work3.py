"""
写一个单例模式的类MusicPlayer

属性：name、list_music(dict{"1": "歌曲名"})、

方法：add_music:通过歌曲名和歌曲的路径，添加到音乐列表的默认路径里（文件可以用.txt文件代替，默认路径自己设置）
"""
class MusicPlayer:

    def __new__(cls, *args, **kwargs):



