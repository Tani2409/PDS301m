# config.py
# 1. Create a tuple
screen_resolution = (1920, 1080)
print(f"Screen resolution tuple: {screen_resolution}")

# 2. Unpack the tuple
width, height = screen_resolution
print(f"Width: {width}, Height: {height}")

# 3. Attempt to modify the tuple (this will raise an error)
try:
    screen_resolution[0] = 1600
except TypeError as e:
    print(f"\nError when trying to change the tuple: {e}")
