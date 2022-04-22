from faker import Faker
fake = Faker(locale='en_CA')

aos_url = 'https://advantageonlineshopping.com/#/'
aos_register_url = 'https://advantageonlineshopping.com/#/register'
new_username = fake.user_name()
email = fake.email()
password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'  # f''    f string
phone_number = fake.phone_number()[5:10]
city = fake.city()
address = fake.street_address()
#address0 = fake.address().replace('\n', '')  # ask Mr.Singh
#address2 = f'{fake.street_address}'
address1 = f'{fake.street_address()}, {city}, {fake.province_abbr()}, {fake.current_country()} {fake.postalcode_in_province()}'
state_province_region = fake.province_abbr()
postal_code = fake.postalcode_in_province()  # from https://faker.readthedocs.io/en/master/locales/en_CA.html




# to take a screenshot while running the test
# res_dir_name = datetime.now().strftime("res_%Y%m%d_%H%M%S")
# n = 0



