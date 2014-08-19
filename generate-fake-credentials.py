#!/usr/bin/env python

import time
import string
import random

# See https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
def generate_fake_aws_access_key_id():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))

def generate_fake_aws_secret_access_key():
	return ''.join(random.choice(string.ascii_uppercase + string.digits + "/+=") for _ in range(40))

output_file = open("fake-" + str(int(time.time() * 1000.0)), "w")
output_file.write("access_key_id = " + generate_fake_aws_access_key_id() + "\n")
output_file.write("secret_acess_key = " + generate_fake_aws_secret_access_key() + "\n")
output_file.close()
