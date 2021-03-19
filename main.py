import instaloader
import sys
	

L = instaloader.Instaloader()
UN = input("Enter username: ")
PW = input("Enter password: ")

try:
	L.login(UN,PW)
	profile = instaloader.Profile.from_username(L.context, str(UN))
except:
	print("\n", "\n", "Username and Password dont match", "\n")
	sys.exit()

#tt = input("Would you like to include verified users in this search? (y/n): ")

print("\n", "\n", "Data available to retrieve: ", "\n", "~Users not following you back~","\n", "~Users you're not following back~", "\n")

option = input("What data would you like to see? ")



#variables
followers = []
following_1 = []
not_back = []
includeVerified = False


def all():
	print("0% done")
	for followee in profile.get_followers():
		followers.append(followee.username)
	print("50% done")
	for following in profile.get_followees():
		following_1.append(following.username)
	print("75% done")
	for i in following_1:
		if i in following_1 and i not in followers:
			not_back.append(i)


def notall():
	print("0% done")	
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
	


if includeVerified == True:
	all()
	for i in not_back:
		print(i)
	print(len(not_back))	

else:
	notall()
	for i in not_back:
		print(i)
	print(len(not_back))
	




