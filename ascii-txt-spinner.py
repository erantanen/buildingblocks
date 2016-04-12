
'''
a silly spinning text mechanism
or printing of periods?
'''


from sys import stdout
from time import sleep

# for i in range(1,20):
#     stdout.write("\r%d" % i)
#     stdout.flush()
#     sleep(1)
# stdout.write("\n")


list_spin1 = ['-', '/', '|', '\\', '-', '/', '|', '\\', '-', '/', '|', '\\' ]


# for i in list_spin:

# for i in range(33, 47+1):
#     i = chr(i)
#     stdout.write("\r%s" % i)
#     stdout.flush()
#     sleep(.5)
#
# stdout.write("\n")

# while True:
#     for elm in range(40):
#         print(".", end=" ")
#
#     print("\n")


from sys import stdout
from time import sleep

for i in range(1,20):
    stdout.write("\r%d" % i)
    stdout.flush()
     sleep(1)
 stdout.write("\n")