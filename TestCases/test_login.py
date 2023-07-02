import time

from PageObjects.LoginPage import LogInPage
from Utilities.ReadProperties import ReadPropeties
from Utilities.log import LogGenerator


class Test_logInPage:
    baseUrl=ReadPropeties.getUrl()
    userName=ReadPropeties.getUsername()
    Password=ReadPropeties.getPassword()
    log=LogGenerator.loggen()

    def test_HomePage_title_001(self,setup):
        self.log.info("TestCase test_HomePage_title_001 started... ")
        self.driver=setup
        self.log.info("Driver Initializing is Done... ")
        self.driver.get(self.baseUrl)
        self.log.info("Opening the Url is Done... ")
        act_title=self.driver.title
        self.log.info("Capturing Title is Done... ")
        time.sleep(10)
        exp_title="GitHub: Let’s build from here · GitHub"
        if act_title==exp_title:
            self.log.info("TestCase test_HomePage_title_001 Passed... ")
            self.driver.save_screenshot(".\\Screenshots\\test_HomePage_title_001Pass.png")
            assert True
            self.driver.close()
        else:
            self.log.info("TestCase test_HomePage_title_001 Failed... ")
            self.driver.save_screenshot(".\\Screenshots\\test_HomePage_title_001Pass.png")
            self.driver.close()
            assert False

    def test_login_002(self,setup):
        self.log.info("TestCase test_login_002 Started... ")
        self.driver = setup
        self.log.info("Driver Initializing is Done... ")
        self.driver.get(self.baseUrl)
        self.log.info("Opening the Url is Done... ")
        self.lp=LogInPage(self.driver)
        time.sleep(5)
        self.lp.getSignLink()
        self.log.info("Get SignInLink successfully... ")
        time.sleep(6)
        self.lp.getUsername(self.userName)
        self.log.info("Get UserName successfully... ")
        time.sleep(5)
        self.lp.getPassword(self.Password)
        self.log.info("Get Password successfully... ")
        self.lp.getSignbtn()
        self.log.info("Get getSignbtn successfully... ")
        time.sleep(5)
        act_title=self.driver.title
        self.log.info("Capturing Title is Done... ")
        exp_title="GitHub"
        if act_title==exp_title:
            self.log.info("TestCase test_login_002 Passed... ")
            self.driver.save_screenshot(".\\Screenshots\\test_login_002Pass.png")
            assert True
        else:
            self.log.info("TestCase test_login_002 Failed... ")
            self.driver.save_screenshot(".\\Screenshots\\Fail.png")
            assert False
        time.sleep(5)
        self.lp.getMenuButton()
        self.log.info("Get getMenuButton successfully... ")
        time.sleep(10)
        self.lp.getSingOutbtn()
        self.log.info("Get getSingOutbtn successfully... ")
        time.sleep(10)
        self.lp.getConSignOut()
        self.log.info("Get getConSignOut successfully... ")
        time.sleep(5)
        self.driver.close()




