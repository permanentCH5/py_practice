import math
def main():
	# We suppose that there is one infected on the first day.
	l_infected_people = []
	n_day = 1
	patient = [1,0,0] # [if sick, latency(days) , days in hospital]
	l_infected_people.append(patient)
	while 1:
		n_day = n_day + 1
		

		if n_day % 5 == 1:
			n_already_infected = 0
			for patient in l_infected_people:
				if patient[0] == 1:
					n_already_infected = n_already_infected + 1
			# new_patient = [1,-1,0]
			for i in range(0,n_already_infected):
				l_infected_people.append([1,-1,0])
				l_infected_people.append([1,-1,0])

		# print (n_day)

		for i in range(0,len(l_infected_people)):
			patient = l_infected_people[i]
			# print (l_infected_people)
			# print (patient)
			# print(i)

			if patient[0] == 1:
				l_infected_people[i][1] = patient[1] + 1

			# print (l_infected_people)

			if patient[1] == 14 and patient[0] == 1:
				l_infected_people[i][0] = 0
				l_infected_people[i][2] = -1


		for i in range(0,len(l_infected_people)):
			patient = l_infected_people[i]
			# print(patient)

			if patient[0]==0:
				l_infected_people[i][2] = l_infected_people[i][2] + 1
			if patient[2]>10:
				l_infected_people[i][2] = 10

		# print (l_infected_people)


		if n_day % 30 == 1:
			n_out = 0
			for i in range(0,len(l_infected_people)):
				if l_infected_people[i][2]==10:
					n_out = n_out +1
			print(n_day)
			print(n_out)
		if n_day == 61 :
			break
		

if __name__ == '__main__':
	main()