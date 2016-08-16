print "YOLO"
try:
	action = argv[1]
	branch = argv[2]
	print "action", action.split()
	print "branch", branch
	if action.split()[0]=="merge":
		exit(1)
	if action.split()[1:] and branch not in action.split()[1:]:
		exit(1)
	exit(0)
except:
	exit(1)

