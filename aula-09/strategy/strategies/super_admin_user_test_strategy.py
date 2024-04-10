from strategies.user_test_strategy import UserTestStrategy

class SuperAdminUserTestStrategy(UserTestStrategy):
    username = "superadmin"

    def verify_home_page_message(self):
        assert "Bem-vindo, super admin!" in self.driver.page_source