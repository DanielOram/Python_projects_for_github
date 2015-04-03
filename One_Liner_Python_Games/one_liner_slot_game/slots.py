__author__ = 'Daniel Oram'

#make sure to run this from the cmd else you may not see the slots effect.
#had to use numbers as some systems don't support unicode suits...
import random;p=lambda:random.choice("1");[print('|'.join([p(),p(),p()]),end='\r') for i in range(8**5)]