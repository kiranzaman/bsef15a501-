import time
#function to read data from the file 
def data_read():
	f=open('file1.txt')
	#read data separated by white space 
	line=f.readline().split()
	while line:
		#dictionary to store data i.e., process number arrival time and burst time 
		dictionary = {}
		dictionary[line[-12]]=line[-11]
		dictionary[line[-10]]=line[-9]
		dictionary[line[-8]]=line[-7]
		dictionary[line[-6]]=line[-5]
		dictionary[line[-4]]=line[-3]
		dictionary[line[-2]]=line[-1]
		dict.append(dictionary)
		line=f.readline().split()
	f.close()
#function to find if there is some process in the waiting queue 
def inWaitingqueue(pname):
	#traverse whole waiting queue and see if the perticular process exists 
	for i in range(0,len(wait_queue)):
		if(wait_queue[i]["pn"] == pname) :
			return True
	return False
#function to see if any process is in ready queue 
def inreadyqueue(pname):
#traverse the ready queue and see if the process exists 
	for i in range(0,len(ready_queue)):
		if(ready_queue[i]["pn"] == pname) :
			return True
	return False
#function to find the process with minimum of the return time from the waiting list after the io burst 
def find_min() :
	minv = int(waiting_list[0]["return_time"])
	new_process = 0
	for n in range(0,len(waiting_list)):
		if int(waiting_list[n]["return_time"]) < minv:
			minv = int(waiting_list[n]["return_time"])
			new_process = n
	return new_process	
#function to update the ready queue with respect to to arrival time of the processes, their burst time, time quantum, io bursts 
def update_ready_queue(check):
	j=0
	dictionary = {'execution_time':0,'ending_time':0,'iotime':0}
	#loop for the total no of processes 
	for i in range(0,len(queue)):
		#condition to check if burst time is greater than zero and no process is coming from waiting queue or ready queue 
		if int(queue[i]["bt"]) > 0 and inWaitingqueue(queue[i]["pn"]) == False and int(queue[i]["at"]) <= current_time and inreadyqueue(queue[i]["pn"]) == False :
			#then update the ready queue 
			ready_queue.append(queue[i])
			#process will be executed as much it has time quantum
			dictionary["execution_time"] = queue[i]["time_quantum"]
			#if the current burst is to be stopped and the process has to go for input/output 
			if int(queue[i]["current_burst"]) == 0 :
				dictionary["iotime"] = "in"
			else:
				dictionary["iotime"] = queue[i]["current_burst"]
			#if burst time is the quantum time then it will be its ending time and terminated 
			if queue[i]["bt"] < queue[i]["time_quantum"] :
				dictionary["ending_time"] = queue[i]["bt"]
			elif int(queue[i]["current_burst"]) == 0 :
				dictionary["ending_time"] = queue[i]["time_quantum"]
			elif  q[i]["bt"] >= q[i]["time_quantum"] and queue[i]["current_burst"] <= queue[i]["time_quantum"] and queue[i]["current_burst"] != '0' :
				dictionary["ending_time"] = queue[i]["current_burst"]
			else :
				dictionary["ending_time"] = queue[i]["time_quantum"]
			list_time.append(dictionary)
	dictionary = {'execution_time':0,'ending_time':0,'iotime':0}
	for j in range(0,len(waiting_list)) :
		val = find_min()
		if waiting_list[val]["return_time"] <= current_time :
			dictionary["execution_time"] = waiting_list[val]["execution_time"]
			dictionary["iotime"] = wait_queue[val]["current_burst"]
			if waiting_list[val]["execution_time"] < wait_queue[val]["current_burst"] :
				dictionary["ending_time"] = waiting_list[val]["execution_time"]
			else :
				dictionary["ending_time"] = wait_queue[val]["current_burst"]
			list_time.append(dictionary)
			ready_queue.append(wait_queue[val])
			print wait_queue[val]["pn"], " is now returning from waiting queue at ", waiting_list[val]["return_time"]
			del wait_queue[val]
			del waiting_list[val]
	if check == True :
		ready_queue.append(ready_queue[0])
		list_time.append(li[0])
		del ready_queue[0]
		del list_time[0]	
#function to update waiting queue 		
def update_waiting_queue():
	wait_queue.append(ready_queue[0])
	dictionary = {'pn':0,'return_time':0,'execution_time':0}
	dictionary["return_time"] = int(ready_queue[0]["ioburst"])+current_time
	dictionary["execution_time"] = list_time[0]["execution_time"]
	waiting_list.append(dictionary)
	#function to print process no and turn around time 
def printfun() :
	print "process name\tturn around time"
	for number in range (0,len(queue)) :
		print output[number]["pn"],"	  	    ",output[number]["turn_around"]
#main function 
if __name__ == "__main__" :
	dict = []
	queue = []
	ready_queue = []
	list_time = []
	wait_queue = []
	waiting_list = []
	check_for_time = True
	current_time = 0
	output = []
	data_read()
	print dict
	#sort with respect to the process' arrival time 
	queue = sorted(di, key = lambda k: int(k["at"]))
	update_ready_queue(False)
	count = 0
	while count != len(queue) :
		if len(ready_queue) != 0 :
			if list_time[0]["ending_time"] != '0' :
				print ready_queue[0]["pn"], " execution started for ",list_time[0]["ending_time"], "sec at time ", current_time
			var = 0
			while var != int(list_time[0]["ending_time"]) :
				current_time = current_time +1
				update_ready_queue(False)
				var = var+1
			list_time[0]["execution_time"] = str(int(list_time[0]["execution_time"])-int(list_time[0]["ending_time"]))
			
			if int(list_time[0]["execution_time"]) == 0 and list_time[0]["iotime"] > '0' :	
				list_time[0]["execution_time"] = ready_queue[0]["time_quantum"]
			if list_time[0]["iotime"] != 'in':
				list_time[0]["iotime"] = str(int(list_time[0]["iotime"])-int(list_time[0]["ending_time"]))
			ready_queue[0]["bt"] = str(int(ready_queue[0]["bt"])-int(list_time[0]["ending_time"]))
			if list_time[0]["iotime"] <= list_time[0]["execution_time"] and list_time[0]["iotime"] != "in" :
				list_time[0]["ending_time"] = list_time[0]["iotime"]
			elif list_time[0]["execution_time"] <= ready_queue[0]["current_burst"] :
				list_time[0]["ending_time"] = list_time[0]["execution_time"]
			elif ready_queue[0]["bt"] <= list_time[0]["execution_time"] :
				list_time[0]["ending_time"] = ready_queue[0]["bt"]
			else :
				list_time[0]["ending_time"] = ready_queue[0]["current_burst"]
			check_for_time =  True
			
			if int(ready_queue[0]["current_burst"]) != 0 and int(ready_queue[0]["bt"]) > 0 and list_time[0]["iotime"] == '0' :
				print ready_queue[0]["pn"], " going to waiting queue for ", ready_queue[0]["ioburst"], "sec at time ", current_time
				check_for_time = False
				update_waiting_queue()
				del ready_queue[0]
				del list_time[0]
			if check_for_time == True and int(ready_queue[0]["bt"]) <= 0 :
				print ready_queue[0]["pn"], "execution completed" 
				out_dic = {'pn':0,'turn_around':0}
				out_dic['turn_around'] = (current_time-int(ready_queue[0]["at"]))
				out_dic['pn'] = ready_queue[0]["pn"]
				output.append(out_dic)
				count = count + 1
				del ready_queue[0]
				del list_time[0]
				check_for_time =  False
			update_ready_queue(check_for_time)
			while len(ready_queue) == 0 and len(queue) != count :
				current_time=current_time+1
				update_ready_queue(False)
		while len(ready_queue) == 0 and len(queue) != count :
				update_ready_queue(False)
				current_time=current_time+1
	printfun()
