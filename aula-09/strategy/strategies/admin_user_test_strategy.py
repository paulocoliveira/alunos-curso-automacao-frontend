from strategies.user_test_strategy import UserTestStrategy

class AdminUserTestStrategy(UserTestStrategy):
    username = "admin"

    def verify_home_page_message(self):
        assert "Bem-vindo, administrador!" in self.driver.page_source