from faker import Faker
fake = Faker()

fake.name()
name=fake.name()
print(name)
# print(fake.text())
address=fake.address()
print(address)
card = fake.credit_card_full()
print(card)