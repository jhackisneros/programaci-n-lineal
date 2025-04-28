import subprocess

class Launcher:
    @staticmethod
    def iniciar():
        subprocess.run(["python", "interfaz/gui.py"])

if __name__ == "__main__":
    Launcher.iniciar()
