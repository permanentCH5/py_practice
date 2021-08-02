import math
def main():
	# We suppose that there is one infected
	n_infected_people = 1
	n_day = 1
	while 1:
		n_day = n_day + 5
		n_infected_people = 2*n_infected_people + n_infected_people
		if n_day % 30 == 1:
			print(n_infected_people)
		if n_day == 61 :
			break
		

if __name__ == '__main__':
	main()