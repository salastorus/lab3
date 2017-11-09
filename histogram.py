import matplotlib.pyplot as plt
from client_get_friends_ages import ClientGetFriendsAges
from get_user_id import  GetUserId


id = GetUserId("salastorus").execute()

arr = ClientGetFriendsAges(id)
list = arr.execute()
print(sorted(list))


plt.hist(list, range(min(list), max(list)))
plt.show()

