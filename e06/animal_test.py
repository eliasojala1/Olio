from animal import Animal
from mammal import Mammal
from wolf import Wolf
from bird import Bird
from dog import Dog

def run_a_tests():
    a1 = Animal(6, species=1)  # an insect?
    a2 = Animal(4, species=6000)  # a cow?
        
    a1.make_sound()
    print(a1.number_of_legs())

    a2.make_sound()
    print(a2.number_of_legs())


def run_b_tests():
    a3 = Mammal()
    a4 = Bird()
    wolf1 = Wolf("Raasinkorpi")
        
    make_it_do_the_sound(a3)
    make_it_do_the_sound(a4)
    make_it_do_the_sound22(a4)
    make_it_do_the_sound(wolf1)
    
    print(a3.number_of_legs())



def make_it_do_the_sound(any_animal:Animal):
    any_animal.make_sound()


def make_it_do_the_sound22(any_bird:Bird):
    any_bird.make_sound()



def run_c_tests():
    a4 = Wolf("Raasinkorpi")
        
    a4.make_sound()
    print(a4.number_of_legs())



def run_d_tests():
    a5 = Bird()
        
    a5.make_sound()
    print(a5.number_of_legs())

def run_e_tests():

    a2 = Mammal()
    a2.make_sound()
    print(a2.number_of_legs())
    a2._species = 7000
    print(a2.get_species())

    a3 = Bird()
    a3.make_sound()
    print(a3.number_of_legs())
    a3._species = 12000
    print(a3.get_species())

    a4 = Wolf("Grey wolf")
    a4.make_sound()
    print(a4.number_of_legs())
    a4._species = 4
    print(a4.get_species())

def run_f_tests():
    dog1 = Dog()
    
    print("* Testing Dog class *")
    dog1.make_sound()
    print("Legs:", dog1.number_of_legs())
    print("Species:", dog1.get_species())
    dog1.wag_tail()

def test_g_tests():
    try:
        a = Animal(-4, 100)  # Negatiivinen jalka-arvo
    except AssertionError:
        print("AssertionError caught in Animal for invalid number_of_legs")

print("a-tests:")
run_a_tests()

print()
print("b-tests:")
run_b_tests()

print("e-tests:")
run_e_tests()

print("f-tests:")
run_f_tests()

print("g-tests:")
test_g_tests()

"""
print()
print("c-tests:")
run_c_tests()

print()
print("d-tests:")
run_d_tests()
"""