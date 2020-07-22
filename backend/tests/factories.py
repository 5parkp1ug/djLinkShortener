import random

import factory
from django.contrib.gis.geos import Point
from factory import fuzzy, lazy_attribute
from factory.fuzzy import BaseFuzzyAttribute
from faker import Faker
from faker.utils.text import slugify

from accounts.models import User, Address


class UserFactory(factory.DjangoModelFactory):
	"""
	Factory for User accounts
	"""
	username = factory.lazy_attribute(lambda o: slugify(o.first_name + '.' + o.last_name))
	email = factory.lazy_attribute(lambda o: '%s@petsearch.in' % o.username)
	mobile_number = '+919876543210'
	gender = fuzzy.FuzzyChoice(User.GENDER_CHOICES, getter=lambda c: c[0])
	is_staff = False

	@lazy_attribute
	def first_name(self):
		faker = Faker()
		return faker.first_name_male() if self.gender is User.MALE else faker.first_name_female()

	@lazy_attribute
	def last_name(self):
		faker = Faker()
		return faker.last_name_male() if self.gender is User.MALE else faker.last_name_female()

	generic_cart = None

	class Params:
		has_cart = factory.Trait(
			generic_cart=factory.RelatedFactory('tests.restaurant.factories.GenericCartFactory', 'user')
		)

	class Meta:
		model = User


class AddressFactory(factory.DjangoModelFactory):
	"""
	Factory for User Address
	"""
	user = factory.SubFactory(UserFactory)

	type = fuzzy.FuzzyChoice(['Home', 'Work', 'Friend'])
	default = factory.Faker('pybool')

	longitude = factory.Faker('longitude')
	latitude = factory.Faker('latitude')

	house = factory.Faker('secondary_address')
	landmark = factory.Faker('street_name')
	area = factory.Faker('street_address')
	address = factory.Faker('address')
	city = factory.Faker('city')
	state = factory.Faker('state')
	pin_code = factory.LazyFunction(lambda: random.randint(111111, 999999))

	class Meta:
		model= Address
