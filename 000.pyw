import os

mypath = os.path.dirname(os.path.realpath(__file__))
old_filename = __file__
old_number = int(old_filename[-7:-4])
new_number = old_number + 1
if new_number < 10:
    new_number = '00' + str(new_number)
elif new_number < 100:
    new_number = '0' + str(new_number)
elif new_number < 1000:
    new_number = str(new_number)

new_filename = mypath + '/' + new_number + '.pyw'

os.rename(old_filename, new_filename)