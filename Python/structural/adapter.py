from abc import ABCMeta, abstractmethod

class IMacOSGame(metaclass=ABCMeta):
    @abstractmethod
    def play_on_mac(self) -> str:
        pass

class WindowsGame:
    def play_on_windows(self) -> bytes:
        return "Playing game on Windows".encode('utf-8')

class WindowsToMacAdapter(IMacOSGame):
    def __init__(self, windows_game: WindowsGame) -> None:
        self._windows_game = windows_game

    def play_on_mac(self) -> str:
        windows_output = self._windows_game.play_on_windows()
        mac_output = windows_output.decode('utf-8')
        return mac_output.encode('iso-8859-1').decode('iso-8859-1')

def play_game_on_mac(game: IMacOSGame) -> None:
    print(game.play_on_mac())

if __name__ == "__main__":
    windows_game = WindowsGame()
    adapted_game = WindowsToMacAdapter(windows_game)
    
    play_game_on_mac(adapted_game)
