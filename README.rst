Cryptopals Solutions
====================

These are my solutions to the NCC Group (formerly Matasano Security) `Cryptopals
crypto challenges <https://cryptopals.com/>`_. To download and run them, do:

.. code:: sh

   git clone https://github.com/brianmwaters/cryptopals.git
   cd cryptopals
   virtualenv --python=pypy3 env/ # PyPy recommended, but not required
   source env/bin/activate
   pip install --requirement requirements.txt
   pytest
