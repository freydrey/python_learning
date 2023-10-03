import time

currentTime = time.clock()
print("Hello")
print("World")
pastTime = time.clock()
print(pastTime-currentTime)

print("1")
time.sleep(3)
print("2")

for i in range(1,11):
    print(i)
    time.sleep(i)