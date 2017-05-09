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
	f=open('file.txt')
	i=0
	current_time=0
	st=0
	c1=0
	j=0
	ind=0
	k=0
	dict =[]
	q=[]
	turn_around= []
	wait = []
	process = []
	count=data_read()
	print count
	#sort the list with respect to their burst time as sjf proceeds according to the shortest job(BT)
	nlist=sorted(dict, key = lambda k: k['bt'])
	while i < count:
		check = False
		q = sorted(nlist, key = lambda k: int(k["bt"]))
		j=0
		nlist = q
		while check == False and j<count :
			if (int(q[j]["at"]) < current_time or int(q[j]["at"]) == current_time):
				process_entered = j
				check = True
			j=j+1
		time1=int(q[process_entered]["bt"])
		#once start , the process will execute to completion as sjf is non premptive 
		print(q[process_entered]["pn"]), "execution started"
		print "Process is going to execute for ",time1," seconds."
		#nothing else will be done untill this process is in execution 
		time.sleep(time1)
		print "Execution completed"
		#update waiting time 
		wait.append(current_time-int(q[process_entered]["at"]))
		current_time =current_time + int(q[process_entered]["bt"])
		#TOT=FT-AT
		#here finish time is the current time 		
		turn_around.append(current_time-int(q[process_entered]["at"])) 
		process.append(q[process_entered]["pn"])
		nlist[process_entered]["bt"]=str(100)
		i=i+1
	#call print function to print the turn around time waiting time and process number 
	print_func()
