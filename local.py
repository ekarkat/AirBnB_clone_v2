from invoke import run as local
from datetime import datetime

# A python script to run commands locally using local
# Example local("ls")


# date = datetime.utcnow()
# file = "versions/web_static_{}{}{}{}{}{}".format(date.year,
# 													date.month,
# 													date.day,
# 													date.hour,
# 													date.minute,
# 													date.second)

# local("mkdir -p versions")
# try:
# 	local("tar -czf {}.tgz web_static".format(file))
# 	print(file)
# except Exception:
# 	print("Error")

name_pattern = "web_static_"

files = local("ls versions | grep web_static_ | sort -r")

print ("----")
print((files.stdout))

fool = files.stdout.split("\n")

print(fool)

print("-----------")


n = 3

for i in range(n):
	# if fool[-1] == "":
	# 	fool.pop()
	# local("rm versions/{}".format(fool.pop()))
	print(i)