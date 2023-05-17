from sre_parse import State
from data.data import Person
from faker import Faker
import random

faker_en = Faker('En')

def generate_person():
    def generate_state():
        states = ['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
        return random.choice(states)

    def generate_city(state):
        if state == 'NCR':
            cities = ['Delhi', 'Gurgaon', 'Noida']
        elif state == 'Uttar Pradesh':
            cities = ['Agra', 'Lucknow', 'Merrut']
        elif state == 'Haryana':
            cities = ['Karnal', 'Panipat']
        elif state == 'Rajasthan':
            cities = ['Jaipur', 'Jaiselmer']
        else:
            cities = []
        return random.choice(cities)

    generated_state = generate_state()
    return Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        mobile=faker_en.msisdn(),
        subject='English',
        state=generated_state,
        city=generate_city(generated_state)
    )