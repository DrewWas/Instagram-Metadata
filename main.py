import instaloader


L = instaloader.Instaloader()
UN = input("Enter username: ")
PW = input("Enter password: ")

L.login(UN,PW)

profile = instaloader.Profile.from_username(L.context, str(UN))

followers = []
n = 0

for followee in profile.get_followers():
	followers.append(followee.username)
	n = n + 1

print(followers) 
print(len(followers))
