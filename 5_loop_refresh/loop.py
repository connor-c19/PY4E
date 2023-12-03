import time

while True:
    code = input("Please enter the access code:\n")
    if code != 'access code':
        print("incorrect")
        continue
    break

n = 5
while n > 0: 
    print("shutting down in", n)
    n -= 1
    time.sleep(1)


print("wait...need to finsih some things up...\n")
time.sleep(1)
print("ok, I'm ready")
for i in range(5, 0, -1):
    print("shutting down in", i)
    time.sleep(1)
