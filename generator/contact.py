import random
import string
from model.contact import Contact
import os.path
import jsonpickle
import getopt
import sys

__author__ = "Grzegorz Holak"

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of Contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " "
    #  + string.punctuation to not fail tests as we know that it is not working correctly with this chars
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


def random_email(prefix, max_len_name, max_len_domain):
    symbols = string.ascii_letters + string.digits
    name = "".join([random.choice(symbols) for i in range(random.randrange(max_len_name))])
    domain = "".join([random.choice(symbols) for i in range(random.randrange(max_len_domain))])
    end = "".join([random.choice(string.ascii_lowercase) for i in range(1, 3)])
    return prefix + "_" + name + "@" + domain + "." + end


def random_phone(prefix, max_len):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


testdata = [
    Contact(first_name=random_string("name", 10), last_name=random_string("lastname", 20)
            , email=random_email("email1", 10, 10), email2=random_email("email2", 10, 15)
            , email3=random_email("e3", 15, 21), address=random_string("address", 50)
            , mobile_phone=random_phone("mob", 10), work_phone=random_phone("work", 10)
            , home_phone=random_phone("home", 10), home_phone2=random_phone("home2", 11))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
