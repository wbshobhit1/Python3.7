f1 = open("eyes.txt")

try:
    f = open("water.txt")

except Exception as e:
    print(e)

else:
    print("This will run only if except is not running")
finally:
    print("Run this anyway...")
    f.close()
    f1.close()
print("Important to run")
