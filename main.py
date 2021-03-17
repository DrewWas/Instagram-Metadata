import instaloader


L = instaloader.Instaloader()
UN = input("Enter username: ")
PW = input("Enter password: ")

L.login(UN,PW)

profile = instaloader.Profile.from_username(L.context, str(UN))

followers = []
n = 0

print("0% done")

for followee in profile.get_followers():
	followers.append(followee.username)


following_1 = []
q = 0

print("50% done")

for following in profile.get_followees():
	following_1.append(following.username)
	q = q + 1


print("75% done")

not_back = []

for i in following_1:
	if i in following_1 and i not in followers:
		not_back.append(i)

for i in not_back:
	print(i)
print(len(not_back))


