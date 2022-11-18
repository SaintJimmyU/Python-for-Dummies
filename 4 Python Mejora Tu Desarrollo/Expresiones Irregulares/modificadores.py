import re

regex = re.compile(r"ay",re.IGNORECASE)
print(regex.search("GuaYAquil"))
print(regex.search("GuaYAquil").group())
