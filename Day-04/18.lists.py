states_of_america = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Conne"]
print(states_of_america[0])
print(states_of_america[-1])

states_of_america[1] = "aalubama"
#this shows that list is immutable and can be changed
print(states_of_america)

states_of_america.append("angelaland")
#it is for adding new items in the list
print(states_of_america)

states_of_america.extend(["delhi","mumbai"])
#it is used for adding a list to another list
print(states_of_america)