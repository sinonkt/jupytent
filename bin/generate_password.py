#!/usr/bin/env python3
import sys
from notebook.auth import passwd; 
__, plain_text_password = sys.argv
print(passwd(plain_text_password, algorithm='sha1'))