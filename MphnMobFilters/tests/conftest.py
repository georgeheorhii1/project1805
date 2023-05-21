from MphnMobFilters.pages.maifonua import maifon_ua
from MphnMobFilters.pages.maifonru import maifon_ru
from MphnMobFilters.pages.mobua import mob_ua
from MphnMobFilters.pages.mobru import mob_ru

data = input("Enter the test name(Variants are following: maifon.ua, maifon.ru, mob.ua, mob.ru: ")

if data == "maifon.ua":
    test_1 = maifon_ua()
    test_1.run_ua()

if data == "maifon.ru":
    test_2 = maifon_ru()
    test_2.run_ru()

if data == "mob.ua":
    test_3 = mob_ua()
    test_3.run_mob_ua()

if data == 'mob.ru':
    test_4 = mob_ru()
    test_4.run_mob_ru()
else:
    print("Choose the store. List of the tests above. ")
