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
	file = open(str(UN)+ "_followers.txt", "a+")
	file.write(followers[n])
	file.write("\n")
	file.close()
	print(followers[n])
	n = n + 1


