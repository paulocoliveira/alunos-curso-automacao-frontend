from selenium import webdriver

class WebDriverSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = webdriver.Chrome()
            cls._instance.maximize_window()
        return cls._instance

    @classmethod
    def quit_instance(cls):
        if cls._instance:
            cls._instance.quit()
            cls._instance = None