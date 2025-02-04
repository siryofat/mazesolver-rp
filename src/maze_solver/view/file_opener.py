from abc import ABC, abstractmethod
import platform
import tempfile
from pathlib import Path
import subprocess
import shutil
import os
import time
import webbrowser

class FileOpenerStrategy(ABC):
    @abstractmethod
    def open_file(self, content: str) -> None:
        pass

class LinuxFileOpener(FileOpenerStrategy):
    def open_file(self, content: str) -> None:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.html', delete=False) as temp_file:
            temp_file.write(content)
            temp_file.flush()
            subprocess.run(['xdg-open', temp_file.name])
            time.sleep(2)  # Give time for the browser to open the file
        os.unlink(temp_file.name)

class WSLFileOpener(FileOpenerStrategy):
    def open_file(self, content: str) -> None:
        if not shutil.which('wslpath') or not shutil.which('wslview'):
            print("Error: wslpath or wslview not found. Please install wslu package.")
            return

        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.html', delete=False) as temp_file:
            temp_file.write(content)
            temp_file.flush()
            try:
                windows_path = subprocess.check_output(['wslpath', '-w', temp_file.name], text=True).strip()
                subprocess.run(['wslview', windows_path], check=True)
                time.sleep(2)  # Give time for the browser to open the file
            except subprocess.CalledProcessError as e:
                print(f"Error opening file: {e}")
            finally:
                os.unlink(temp_file.name)

class MacOSFileOpener(FileOpenerStrategy):
    def open_file(self, content: str) -> None:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.html', delete=False) as temp_file:
            temp_file.write(content)
            temp_file.flush()
            subprocess.run(['open', temp_file.name])
            time.sleep(2)  # Give time for the browser to open the file
        os.unlink(temp_file.name)

class WindowsFileOpener(FileOpenerStrategy):
    def open_file(self, content: str) -> None:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.html', delete=False) as temp_file:
            temp_file.write(content)
            temp_file.flush()
            os.startfile(temp_file.name)
            time.sleep(2)  # Give time for the browser to open the file
        os.unlink(temp_file.name)

class DefaultFileOpener(FileOpenerStrategy):
    def open_file(self, content: str) -> None:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.html', delete=False) as temp_file:
            temp_file.write(content)
            temp_file.flush()
            webbrowser.open(f'file://{temp_file.name}')
            time.sleep(2)  # Give time for the browser to open the file
        os.unlink(temp_file.name)

class FileOpener:
    def __init__(self):
        self.opener = self._get_opener()

    def _get_opener(self) -> FileOpenerStrategy:
        system = platform.system()
        if system == "Linux":
            if "microsoft" in platform.uname().release.lower():
                return WSLFileOpener()
            return LinuxFileOpener()
        elif system == "Darwin":
            return MacOSFileOpener()
        elif system == "Windows":
            return WindowsFileOpener()
        else:
            return DefaultFileOpener()

    def open_in_browser(self, content: str) -> None:
        self.opener.open_file(content)