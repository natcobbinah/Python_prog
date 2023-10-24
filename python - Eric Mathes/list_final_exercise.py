guest_lists = ["Romeo","Juliet","Shakespheare","Mary Ann"]
print(f"Hello {guest_lists[0]}, I am inviting you to my end of year party")
print(f"Hello {guest_lists[1]}, I am inviting you to my end of year party")
print(f"Hello {guest_lists[2]}, I am inviting you to my end of year party")

print(f"There is a message from {guest_lists[1]} that he cannot make it to the party")
guest_lists.pop(1)
guest_lists.insert(1, "Duke")

print("New list of invitations")
print(f"Hello {guest_lists[0]}, I am inviting you to my end of year party")
print(f"Hello {guest_lists[1]}, I am inviting you to my end of year party")
print(f"Hello {guest_lists[2]}, I am inviting you to my end of year party")

print("found a bigger dinner table")
guest_lists.insert(0, "Babbage")
guest_lists.insert(2,"Ada")
guest_lists.append("Maverick")

print(f"Hello {guest_lists[0]}, I am inviting you to my end of year party")
print(f"Hello {guest_lists[1]}, I am inviting you to my end of year party")
print(f"Hello {guest_lists[2]}, I am inviting you to my end of year party")
print(f"Hello {guest_lists[3]}, I am inviting you to my end of year party")
print(f"Hello {guest_lists[4]}, I am inviting you to my end of year party")
print(f"Hello {guest_lists[5]}, I am inviting you to my end of year party")
print(f"Hello {guest_lists[6]}, I am inviting you to my end of year party")

print("Sorry a problem with the dinner table")
last_guestNonInvite = guest_lists.pop(6)
print(f"Sorry {last_guestNonInvite}, the table won't arrive on time so the invite is cancelled")

last_guestNonInvite2 = guest_lists.pop(5)
print(f"Sorry {last_guestNonInvite2}, the table won't arrive on time so the invite is cancelled")

print(guest_lists)
del guest_lists[0]
del guest_lists[1]
del guest_lists[2]

print(guest_lists)
del guest_lists[0]
print(guest_lists)
del guest_lists[0]
print(guest_lists)