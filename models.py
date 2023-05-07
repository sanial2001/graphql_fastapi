from collections import namedtuple

Person = namedtuple("Person", ['first_name', 'last_name', 'email', 'age'])

data = {
    1: Person("John", "Doe", "johndoe@gmail.com", "23"),
    2: Person("Jane", "Doe", "janedoe@gmail.com", "24"),
    3: Person("Ross", "Miles", "rossmiles@gmail.com", "21"),
    4: Person("Bruce", "Wayne", "brucewayne@gmail.com", "33"),
}
