import random

#by defualt return value in float
"""x=random.random()
print(x)"""


#return int value
"""x=random.randint(1111,9999)
print(x)"""

captcha=['sdhfg','sjfg','wdesf',"oeoqw",'qwewl','evsdy']
#x=random.choice(captcha)
#print(x)

random.shuffle(captcha)
print(captcha)