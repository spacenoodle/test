try:
	action = argv[1]
	branch = argv[2]
	if action.split()[0]=="merge" or branch not in action.split()[1:]:
		exit(1)
	exit(0)
except:
	exit(1)

