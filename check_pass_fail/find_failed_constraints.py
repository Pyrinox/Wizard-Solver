
#contains ALL constraints
with open("check", "r") as check:
    read_check = []
    for line in check:
        read_check.append(line.strip())


# returns only constraints that passed autograder
# passed is a subset of check
with open("passed", "r") as passed:
    read_passed = []
    for line in passed:
        read_passed.append(line.strip())

failed_constraints = []
for line in read_check:
	if line not in read_passed:
		failed_constraints.append(line)

print(failed_constraints)


# # information we are given
# num_of_wizards = read[0]
# num_of_constraints = read[1]
# constraints = []
# wizards = set()
# for line in read[2:]:
#     for wizard in line.split():
#         wizards.add(wizard)
#     constraints.append(line.split())
# state = list(wizards)