#%%
class Student:
    students = 0 # this is a class attribute
    def __init__(self, name, ta):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        ta.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

# %%
snape = Professor('Snape')
harry = Student('Harry', snape)
# %%
harry.visit_office_hours(snape)
# %%
harry.visit_office_hours(Professor('Hagrid'))
# %%
harry.understanding
# %%
[name for name in snape.students]
# %%
Student('Hermione', Professor('McGonagall')).name
# %%
[name for name in snape.students]
# %%
class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.message = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        if email.recipient_name in self.clients:
            self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds it
        to the clients instance attribute.
        """
        self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
        self.server.register_client(self, self.name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        self.server.send(Email(msg, self.name, recipient_name))

    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox.append(email)
#%%
class Pet():
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')
#%%
class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives
    
    def talk(self):
        """ Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + ' says meow!')
    from doctest import run_docstring_examples
    run_docstring_examples(talk, globals(), True)

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False.
        """
        while self.lives > 0:
            self.lives -= 1
        if self.lives == 0:
            self.is_alive = False

# %%
class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""
    #def __init__(self, name, owner, lives=9):
    # Is this method necessary? Why or why not?

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        print(self.name + ' says meow!')
        print(self.name + ' says meow!')
    run_docstring_examples(talk, globals(), True)
# %%
class A:
    def f(self):
        return 2

    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)

class B(A):
    def f(self):
        return 4

# %%
x, y = A(), B()
x.f()
# %%
B.f()
# %%
x.g(x, 1)
# %%
A.f(x)
# %%
y.g(x, 2)
# %%
class Foo:
    '''
    >>> x = Foo(1)
    >>> x.g(3)
    4
    >>> x.g(5)
    6
    >>> x.bar = 5
    >>> x.g(5)
    10
    '''
    def __init__(self, bar):
        self.bar = bar

    def g(self, num):
        return self.bar + num 
run_docstring_examples(Foo, globals(), True)
# %%
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def helper(f):
        nonlocal n
        n = f(n)
        return n
    return helper
run_docstring_examples(memory, globals(), True)
# %%
