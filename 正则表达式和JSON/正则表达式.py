a = 'C|C++|Java|C#|Python|JavaScript'

# print(a.index('Python') > -1)
#
# print('Python' in a)

import re

print(re.findall('Python', a))


