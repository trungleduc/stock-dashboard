import voila.app
import sys, os

if __name__ == "__main__":
    port = sys.argv[1]
    os.environ["VOILA_APP_PORT"] = port

    v = voila.app.Voila()
    v.notebook_path = "./dashboard.ipynb"
    v.ip = "0.0.0.0"
    v.port = int(port)
    v.initialize()

    v.voila_configuration.preheat_kernel = True
    v.voila_configuration.enable_nbextensions = True
    v.voila_configuration.theme = "dark"
    v.open_browser = False
    v.start()
