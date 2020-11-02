#!/bin/bash

/etc/init.d/postgresql start
/etc/init.d/apache2 start
cd Sploit/

python sploit.py
