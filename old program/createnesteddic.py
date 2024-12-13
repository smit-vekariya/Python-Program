import os
try:
   os.mkdir("s:/python/tb")
except FileExistsError:
    print("file alrady exists")