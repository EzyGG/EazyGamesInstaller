import requests, os, ctypes, sys
import mysql_connection as connect

URL = "http://luzog.xyz:48833/downloads"
PATH = ""


class Attributes:
    app, inst, entry, browse, combobox = None, None, None, None, None


def get_versions():
    connect.execute("SELECT version FROM versions ORDER BY date DESC")
    return [e[0] for e in connect.fetch()]


def verify_admin():
    try:
        try:
            open(PATH + "/.admin", "w").close()
        except FileNotFoundError:
            os.mkdir(PATH)
        finally:
            open(PATH + "/.admin", "w").close()
            os.remove(PATH + "/.admin")
    except PermissionError:
        Attributes.app.destroy()
        # TODO -> note that if you converted you python script into an executable file (using tools like py2exe,
        #  cx_freeze, pyinstaller) then you should use sys.argv[1:] instead of sys.argv in the fourth parameter
        #  https://stackoverflow.com/questions/130763/request-uac-elevation-from-within-a-python-script
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        try:
            if not ctypes.windll.shell32.IsUserAnAdmin():
                exit(0)
        except Exception:
            exit(0)


def dwl(path: str = ""):
    req = requests.get(URL + "/" + path)
    with open(path if ":" in path else (PATH + "/" + path), 'wb') as file:
        file.write(req.content)


def browse_func(x=None):
    from tkinter import filedialog
    Attributes.entry.delete(0, "end")
    Attributes.entry.insert(0, filedialog.askdirectory(parent=Attributes.app, title="Choisissez un dossier"))


def install(x=None):
    global PATH
    PATH = Attributes.entry.get().replace("\\", "/").replace("//", "/")
    verify_admin()
    ver = Attributes.combobox.get()
    Attributes.app.destroy()
    dwl(ver + ".exe")
    os.popen("\"" + PATH + "/" + ver + ".exe\"")
