# ********** 👇 Python Check if String is Datetime 👇 ********** #



# -- 👇 Check DateTime Using parse()  👇 -- #

from dateutil.parser import parse # 👉️ Import parse() module

my_str = "1995-12-12" # 👉️ String

# 👇 Check if my_str is DateTime
try: 
    parse(my_str, fuzzy=False) # 👉️ (fuzzy=False) String is DateTime
    print(True)

except ValueError:
    print(False)

# 👆 Output: True





# -- 👇 Check DateTime Using parse() Year/Month/Day Format 👇 -- #

from dateutil.parser import parse # 👉️ Import parse() module

my_str = "1995/12/12" # 👉️ String

# 👇 Check if my_str is DateTime
try: 
    parse(my_str, fuzzy=False)
    print(True)

except ValueError:
    print(False)

# 👆 Output: True





# -- 👇 Check DateTime Using parse() Year/Month/Day Hours:Minutes 👇 -- #

from dateutil.parser import parse # 👉️ Import parse() module

my_str = "1995/12/12 12:00" # 👉️ String

# 👇 Check if my_str is DateTime
try: 
    parse(my_str, fuzzy=False)
    print(True)

except ValueError:
    print(False)

# 👆 Output: True





# -- 👇 Check DateTime Using parse() Year/Month/Day Hours:Minutes AM/PM format 👇 -- #

from dateutil.parser import parse # 👉️ Import parse() module

my_str = "1995-12-12 12:00am" # 👉️ String

# 👇 Check if my_str is DateTime
try: 
    parse(my_str, fuzzy=False)
    print(True)

except ValueError:
    print(False)

# 👆 Output: True





# -- 👇 Check DateTime Format Using parse()  👇 -- #

from dateutil.parser import parse # 👉️ Import parse() module

my_str = "today is 1995-12-12 12:00am" # 👉️ String

# 👇 Check if my_str is DateTime
try: 
    parse(my_str, fuzzy=False)
    print(True)

except ValueError:
    print(False)

# 👆 Output: False





# -- 👇 Check DateTime Using parse() fuzzy=True 👇 -- #

from dateutil.parser import parse # 👉️ Import parse() module

my_str = "today is 1995-12-12 12:00am" # 👉️ String

# 👇 Check if my_str contains DateTime
try: 
    parse(my_str, fuzzy=True) # 👉️ (fuzzy=True) DateTime in String
    print(True)

except ValueError:
    print(False)

# 👆 Output: True





# -- 👇 Check DateTime Format is Y-M-D Using datetime()  👇 -- #

from datetime import datetime # 👉️ Import datetime() module

my_str = "1995-12-12" # 👉️ String

# 👇 Check if my_str is DateTime
try:
    datetime.strptime(my_str, '%Y-%m-%d')
    print(True)

except ValueError:
    print(False)

# 👆 Output: True





# -- 👇 Cjeck DateTime Format is Year-Month-Day Using datetime()  👇 -- #

from datetime import datetime # 👉️ Import datetime() module

my_str = "1995/12/12" # 👉️ String

# 👇 Check if my_str is Date
try:
    datetime.strptime(my_str, '%Y-%m-%d')
    print(True)

except ValueError:
    print(False)

# 👆 Output: False





# -- 👇 Check DateTime Format is Y-M-D H:M Using datetime()  👇 -- #

from datetime import datetime # 👉️ Import datetime() module

my_str = "1995-12-12 13:50" # 👉️ String

# 👇 Check if my_str is DateTime
try:
    datetime.strptime(my_str, '%Y-%m-%d %H:%S')
    print(True)
    
except ValueError:
    print(False)

# 👆 Output: True






# -- 👇 Check DateTime Format is Y-M-D H:M Using datetime()  👇 -- #

from datetime import datetime # 👉️ Import datetime() module

my_str = "1995-12-12 01:50 AM" # 👉️ String

# 👇 Check if my_str is DateTime
try:
    datetime.strptime(my_str, '%Y-%m-%d %H:%S %p')
    print(True)

except ValueError:
    print(False)

# 👆 Output: True
