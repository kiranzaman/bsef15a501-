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

#function to check whether while at the running of the current process , some new process is entered in the queue 
def check_job(val):
	current_process=0
	new_entered_process=0
	check=False
	while check == False and j<count :
			if (int(q[current_process]["at"]) < val or int(q[current_process]["at"]) == val):
				new_entered_process = current_process
				check = True
			current_process=current_process+1
	return new_entered_process
#function to find the arrival time of the current process 
def search_arrival_time(pn):
	n=0
	arivaltime=0
	while n<count :
		if pn == dict[n]["pn"] :
			arivaltime=int(dict[n]["at"])
		n=n+1
	return arivaltime
	
#function to find the burst time of the current process 
def search_burst_time(pn1):
	m=0
	bursttime=0
	while m<count :
		if pn1 == di[m]["pn"] :
			bursttime=int(di[m]["bt"])
		m=m+1
	return bursttime
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

	i=0
	wt=0
	small_remainder=0
	check_process=0
	execution_time=0
	dict =[]
	q=[]
	nlist=[]
	check1=True
	count=data_read(dict)
	data_read(nlist)
	turn_around=[]
	wait=[]
	process=[]
	while check1== True:
		check1=False
		q = sorted(nlist, key = lambda execution_time: int(execution_time["bt"]))
		nlist = q
		small_remainder=check_job(execution_time)
		check_process=small_remainder
		print(q[small_remainder]["pn"]), "execution started"
#		print "this is going to sleep for ",tim," seconds."
#check if the remaining time of current process is smallest and greater than 0 means it has srt
		while check_process == small_remainder and int(q[small_remainder]["bt"]) >0:
			time.sleep(1)
			execution_time=execution_time+1
			val=int(q[small_remainder]["bt"])
			val=val-1
			q[small_remainder]["bt"]=str(val)
			check_process = check_job(execution_time)

		#see if the process still has burst time left then it will be stopped otherwise completely executed 
		if int(q[small_remainder]["bt"]) > 0:
			print q[small_remainder]["pn"], "execution stopped"
		else:
			print q[small_remainder]["pn"], "execution completed"
			
			wait.append(execution_time-search_arrival_time(q[small_remainder]["pn"])-search_burst_time(q[small_remainder]["pn"]))
	
			turn_around.append(execution_time-search_arrival_time(q[small_remainder]["pn"]))
			process.append(q[small_remainder]["pn"])
			nlist[small_remainder]["bt"]=str(1000)
		n=0
		while n<count :
			if int(nlist[n]["bt"])!=1000:
				check1=True
			n=n+1
	print_func()
