from time import sleep
import pytest
from conftest import *
from hrmpages.Adminpage import AdminPage

@pytest.mark.usefixtures("browser_setup")
class Test_login:


    def setup_class(self):
        self.driver.maximize_window()
        sleep(2)
        self.driver.get(BaseURL)

        self.admin_page = AdminPage(self.driver)

    def test_valid_login(self):
        self.admin_page.login(Username)

    def test_logo_check(self):
        self.admin_page.Logocheck(Username, Password)

    def test_header_check(self):
        self.admin_page.Headercheck()

    def test_mainmenu_check(self):
        self.admin_page.Mainmenucheck()


    def teardown_class(self):
        self.driver.quit()

