#3.4
guests = ['sorokin', 'bobrov', 'lebedev']
message = f"welcome to meeting!"
print(f"Dear, mr.{guests[0].title()} {message}")
print(f"Dear, mr.{guests[1].title()} {message}")
print(f"Dear, mr.{guests[2].title()} {message}")

#3.5
print(f"\nOh sorry, mr.{guests[1].title()} won't be able to come!")
del guests[1]
guests.insert(1, 'karyakin')
print(f"Dear, mr.{guests[0].title()} {message}")
print(f"Dear, mr.{guests[1].title()} {message}")
print(f"Dear, mr.{guests[2].title()} {message}")

#3.6
print(f"\n")
guests.insert(0, 'serebryakov')
guests.insert(2, 'myagkov')
guests.append('filatov')
print(f"Dear, mr.{guests[0].title()} {message}")
print(f"Dear, mr.{guests[1].title()} {message}")
print(f"Dear, mr.{guests[2].title()} {message}")
print(f"Dear, mr.{guests[3].title()} {message}")
print(f"Dear, mr.{guests[4].title()} {message}")
print(f"Dear, mr.{guests[5].title()} {message}")
print(f"Number of guests for meeting: {len(guests)}.")

