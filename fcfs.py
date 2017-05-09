import time
#function to read data from the file 
def data_read():
	total_process=0
	#read data separated by white space 
	line=f.readline().split()
	while line:
		total_process=total_process+1	
		#dictionary to store data i.e., process number arrival time and burst time 
		dictionary = {}
		dictionary[line[-6]]=line[-5]
		dictionary[line[-4]]=line[-3]
		dictionary[line[-2]]=line[-1]
		dict.append(dictionary)
		line=f.readline().split()
	f.close()
	#returns the count of total number of process 
	return total_process
#function to print the output 
def print_func():
	numberOfProcesses=0
	print "process   turn around time   waiting time"
	#loop till total number of processes 
	while numberOfProcesses<count:
		print process[numberOfProcesses],"		",turn_around[numberOfProcesses],"		", wait[numberOfProcesses]
		numberOfProcesses=numberOfProcesses+1
#main function 
if __name__ == "__main__" :
	#read from file 
	f=open('file.txt')
	i=0
	t=0
	waiting_time=0
	burst_time=0
	k=0
	count =0
	dict =[]
	process = []
	#count is for count of total number of processses 
	count=data_read()
	turn_around = []
	wait = []
	#using sort function and sorting the processes with respect to arrival time as the process with the smaller arrival time willl be served first(FCFS)
	nlist=sorted(dict, key = lambda k: k['at'])	
	#loop  for total number of processes 
	while i<count:

		print dict[i]["pn"] ,"execution started"
		burst_time=int(dict[i]["bt"])
		print dict[i]["pn"] ," going to execute for ", burst_time, "seconds"
		#for the completion of burst time , it won't be stopped as its non-premptive 
		while burst_time>0:
			time.sleep(1)
			burst_time=burst_time-1
			t=t+1
		print(dict[i]["pn"]), "execution completed"
		#turnaround time = finish time - arrival time 
		#finish time = waiting time + burst time 
		turn_around.append((waiting_time+int(dict[i]["bt"]))-int(dict[i]["at"]))
		wait.append((waiting_time-int(dict[i]["at"])))
		process.append(dict[i]["pn"])
		i=i+1
		#waiting time updated 
		waiting_time=t
	print_func()
