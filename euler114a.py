import time
start = time.time()

# 12 pieces of red need at least 11 single black spacers
#3x12, 3x11+4, 3x11+5, 3x11+6, 3x10+2x4, 3x10+4+5, 3x9+3*4

# 11 pieces of red need at least 10 single black spacers
#3x11, 3x10+4, 3x10+5, 3x10+6, 3x10+7, 3x10+2x4, 3x10+4+5, 3x9+3*4

# change problem? first figure out pieces

print time.time() - start