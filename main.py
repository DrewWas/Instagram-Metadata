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


print("\n", "\n", "Data available to retrieve: ", "\n", "~Users not following you back~  [0]","\n", "~Users you're not following back~  [1]", "\n")

option = input("What data would you like to see? ")
andVerified = input("Would you like to include verified users? (y/n): ")
print("\n")


#variables
followers = []
following_1 = []
not_back = []


def all():
	print("0% done")
	for followee in profile.get_followers():
		followers.append(followee.username)
	print("50% done")
	for following in profile.get_followees():
		following_1.append(following.username)
	print("75% done")
	print("\n")
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
	print("\n")
	for i in following_1:
		if i in following_1 and i not in followers:
			not_back.append(i)	
	

def whoIDontFollow():
	print("0% done")
	for followee in profile.get_followers():
		followers.append(followee.username)

	print("50% done")
	for following in profile.get_followees():
		following_1.append(following.username)
	print("75% done")
	print("\n")
	for i in followers:
		if i in followers and i not in following_1:
			not_back.append(i)

def whoIDontVerify():
	print("0% done")
	for followee in profile.get_followers():
		followers.append(followee.username)
	print("50% done")
	for following in profile.get_followers():
		if following.is_verified == False:
			following_1.append(following.username)
	print("75% done")
	print("\n")
	for i in followers:
		if i in followers and i not in following_1:
			not_back.append(i)



if "0" in option and "y" in andVerified:
	all()
	for i in not_back:
		print(i)
	print("total - ",  len(not_back))
	print("\n")
	
elif "0" in option and "n" in andVerified:
	notall()
	for i in not_back:
		print(i)
	print("total - ",  len(not_back))
	print("\n")
elif "1" in option and "y" in andVerified:
	whoIDontFollow()
	for i in not_back:
		print(i)
	print("total - ", len(not_back))
	print("\n")
elif "1" in option and "n" in andVerified:
	whoIDontVerify()
	for i in not_back:
		print(i)
	print("total - ", len(not_back))
	print("\n")
else:
	print("Input incorrect", "\n", "~ Please make sure you only enter what is prompted ~", "\n")

	

