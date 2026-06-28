from hashlib import sha384
from secret import FLAG

print(''.join([sha384(c.encode()).hexdigest()[:5] for c in FLAG ]))

# 8a5e675d378d18254a5981deaad14a1ad0e1ad0e95ed472df8bcf6e5335f72df8586b017580a87d840f985f9158ac1075823758237582375823000f40b759a4eb0bcf6ec2b14000f41d0ec17580a87d8f99c575d37883c5049e7e7cdc1d0ec000f41f366

