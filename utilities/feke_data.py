from faker import Faker


class FakeData:

    @staticmethod
    def get_name(localization):
        return Faker(localization).first_name()

    @staticmethod
    def get_last_name(localization):
        return Faker(localization).last_name()

    @staticmethod
    def get_phone_number(localization):
        return Faker(localization).phone_number()

    @staticmethod
    def get_address(localization):
        return Faker(localization).street_address()

    @staticmethod
    def get_city(localization):
        return Faker(localization).city()

    @staticmethod
    def get_post_code(localization):
        return Faker(localization).postcode()

    @staticmethod
    def get_region(localization):
        return Faker(localization).region().lower().replace(" ", "")

    @staticmethod
    def get_email(name):
        return f"{name}@{Faker().free_email_domain()}"

    @staticmethod
    def get_password():
        return Faker().password(10)
