class DashboardLocatorsCollection:
    def __init__(self):
        self.__nav_bar_locator = ('xpath', "//div[@class='header__burger']")

    @property
    def nav_bar_locator(self):
        return self.__nav_bar_locator

    #@setter.nav_bar_locator()
    #def nav_bar_locator(self, new_value):
    #    self.__nav_bar_locator = new_value