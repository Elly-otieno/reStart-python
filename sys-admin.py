'''
Introducing system administration with python

We can use Linux to do many administrative tasks from the terminal, or the Bash command line. 
Python provides several modules that you can also use to run commands on the command line. 
In this lab, we will use os.system() and subprocess.run() to run Bash commands from Python.

In this lab, we will:

 - Use os.system() to run a Bash command
 - Use subprocess.run() to run Bash commands
'''

# Using os.system
import os

os.system("ls")

