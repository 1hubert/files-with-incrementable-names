import os

mypath = os.path.dirname(os.path.realpath(__file__))
old_filename = __file__
old_number = int(old_filename[-7:-4])
new_number = old_number + 1
new_number = str(new_number).zfill(3)

new_filename = mypath + '/' + new_number + '.pyw'

os.rename(old_filename, new_filename)