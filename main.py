import instaloader


L = instaloader.Instaloader()
UN = input("Enter username: ")
PW = input("Enter password: ")
includeVerified = False
tt = input("Would you like to include verified users in this search? (y/n): ")

if tt == "y":
	includeVerified = True
else:
	includeVerified = False


L.login(UN,PW)

profile = instaloader.Profile.from_username(L.context, str(UN))

followers = []
following_1 = []
not_back = []

print("0% done")

def all():

	for followee in profile.get_followers():
		followers.append(followee.username)



	print("50% done")

	for following in profile.get_followees():
		following_1.append(following.username)


	print("75% done")


	for i in following_1:
		if i in following_1 and i not in followers:
			not_back.append(i)




if includeVerified == True:
	all()
	for i in not_back:
		print(i)
	print(len(not_back))	

else:
	for followee in profile.get_followers():
		followers.append(followee.username)
	print("50% done")
	for following in profile.get_followees():
		if following.is_verified == False:
			following_1.append(following.username)
	print("75% done")
	for i in following_1:
		if i in following_1 and i not in followers:
			not_back.append(i)

	for i in not_back:
		print(i)
	print(len(not_back))
	




