import time

t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("enter hours"))
print(hour)

if (hour >= 0 and hhour < 12):
  print("good morning Godx")
elif (hour >= 12 and hour < 17):
  print("good afternoon Godx")
elif (hour >= 17 and hour < 0):
  print("good night Godx")