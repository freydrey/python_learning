keyWord = "hello"

try:
    print(int("Hello"))

#except Exception as e:
#except ValueError:
 
 #   print("got a value error")
except Exception as e:
    print("Other type of error")
    print(str(e))
    #raise
finally:
    print("finally")

print("Past exception")