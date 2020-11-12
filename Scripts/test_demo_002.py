import allure


class Test002:

    @allure.severity(allure.severity_level.BLOCKER)  # 最重要用例
    def test_002_1(self):
        print("\n test_002_1")

    @allure.severity(allure.severity_level.CRITICAL)  # 重要用例
    def test_002_2(self):
        print("\n test_002_2")
        assert 1 + 1 == 3

    @allure.severity(allure.severity_level.NORMAL)  # 一般用例
    def test_002_3(self):
        print("\n test_002_3")

    @allure.severity(allure.severity_level.MINOR)  # 轻微用例
    def test_002_4(self):
        print("\n test_002_4")

    @allure.severity(allure.severity_level.TRIVIAL)  # 忽略用例
    def test_002_5(self):
        print("\n test_002_5")
