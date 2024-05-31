1. The directory name where you are keeping emojiTranslator.cpp, emojiTranslator.hpp, main.py, and setup.py files must be 'emojiTranslator_pythonBinding'.
2. First run the setup.py file by using 'pip install -e .' command. This command installs a Python package.
3. If you want a very emphasize output you can add -vvv flag at the end of the command like 'pip install -e . -vvv'
   Break down of this command:
      pip :  To invoke the pip package manager for installing Python packages
       -e :   This flag tells pip to perform the installation in editable mode means this creates a link between the source code and the installed package.
        . :   The current working directory.
      -vvv: This flag is called verbosity flag, it instruct pip to provide very verbose output during the installation process.

4. If you get a successfull output report (Successfully installed emojiTranslator-0.1) then run 'python3 -m unittest -v main.py' this command.
5. 'python3 -m unittest -v main.py' this command run the unit test cases written in Python using the unittest module and shows verbose output.
6. Break down of this command:
      python3    : This tells which Python interpreter to use.
      -m unittest: This tells Python to run the unittest module as a script. The -m flag signifies execution of a module as a script.
          -v     : This option enables verbose output. You'll see more details about the test run, including the names of test cases and their results (passed or failed).
       main.py   : This is the filename of Python script containing the unit test cases.
