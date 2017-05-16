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
	for i in range(0,len(q)):
		#condition to check if burst time is greater than zero and no process is coming from waiting queue or ready queue 
		if int(q[i]["bt"]) > 0 and inWaitingqueue(q[i]["pn"]) == False and int(q[i]["at"]) <= current_time and inreadyqueue(q[i]["pn"]) == False :
			#then update the ready queue 
			ready_queue.append(q[i])
			#process will be executed as much it has time quantum
			dictionary["execution_time"] = q[i]["time_quantum"]
			#if the current burst is to be stopped and the process has to go for input/output 
			if int(q[i]["current_burst"]) == 0 :
				dictionary["iotime"] = "in"
			else:
				dictionary["iotime"] = q[i]["current_burst"]
			#if burst time is the quantum time then it will be its ending time and terminated 
			if q[i]["bt"] < q[i]["time_quantum"] :
				dictionary["ending_time"] = q[i]["bt"]
			elif int(q[i]["current_burst"]) == 0 :
				dictionary["ending_time"] = q[i]["time_quantum"]
			elif  q[i]["bt"] >= q[i]["time_quantum"] and q[i]["current_burst"] <= q[i]["time_quantum"] and q[i]["current_burst"] != '0' :
				dictionary["ending_time"] = q[i]["current_burst"]
			else :
				dictionary["ending_time"] = q[i]["time_quantum"]
			list.append(dictionary)
	dictionary = {'execution_time':0,'ending_time':0,'iotime':0}
	for j in range(0,len(waiting_list)) :
		val = find_min()
		if waiting_list[val]["return_time"] <= current_time :
			dictionary["execution_time"] = waiting_list[val]["execution_time"]
			dictionary["iotime"] = wait_queue[val]["current_burst"]
			if waiting_list[val]["execution_time"] < wait_queue[val]["current_burst"] :
				d["ending_time"] = waiting_list[val]["execution_time"]
			else :
				d["ending_time"] = wait_queue[val]["current_burst"]
			list.append(dictionary)
			ready_queue.append(wait_queue[val])
			print wait_queue[val]["pn"], " is now returning from waiting queue at ", waiting_list[val]["return_time"]
			del wait_queue[val]
			del waiting_list[val]
	if check == True :
		ready_queue.append(ready_queue[0])
		list.append(li[0])
		del ready_queue[0]
		del list[0]
#function to update waiting queue 		
def update_waiting_queue():
	wait_queue.append(ready_queue[0])
	dictionary = {'pn':0,'return_time':0,'execution_time':0}
	dictionary["return_time"] = int(ready_queue[0]["ioburst"])+current_time
	dictionary["execution_time"] = list[0]["execution_time"]
	waiting_list.append(dictionary)
	
def update_auxilary_queue(current_time, count) :
	processcount = 0 
	for processcount in range(0,len(auxiliary_list)-1) :
		if int(auxiliary_list[0]["ending_time"]) != 0 :
			print auxiliary_queue[0]["pn"], " execution started for ",auxiliary_list[0]["ending_time"], "sec at time ", current_time
			checkendingtime = 0
			while checkendingtime != int(auxiliary_list[0]["ending_time"]) :
				current_time = current_time +1
				update_ready_queue(False)
				checkendingtime = checkendingtime+1
			auxiliary_queue[0]["bt"] = str(int(auxiliary_queue[0]["bt"])-int(auxiliary_list[0]["ending_time"]))
			checkexecution = True
			if int(auxiliary_queue[0]["bt"]) <= 0 :
				print ready_queue[0]["pn"], "execution completed" 
				out_dic = {'pn':0,'turn_around':0}
				out_dic['turn_around'] = (current_time-int(ready_queue[0]["at"]))
				out_dic['pn'] = aq[0]["pn"]
				output.append(out_dic)
				count = count + 1
				checkexecution =  False
				del auxiliary_queue[0]
				del auxiliary_list[0]
			elif int(auxiliary_queue[0]["current_burst"]) != 0 and int(auxiliary_queue[0]["bt"]) > 0 and auxiliary_list[0]["iotime"] == '0' :
				print auxiliary_queue[0]["pn"], " going to waiting queue for ", auxiliary_queue[0]["ioburst"], "sec at time ", current_time
				checkexecution = False
				update_waiting_queue()
				del auxiliary_queue[0]
				del auxiliary_list[0]
			else :
				d1= {'execution_time':0,'ending_time':0,'iotime':0}
				ready_queue.append(auxiliary_queue[0])
				d1["execution_time"] = auxiliary_queue[0]["time_quantum"]
				if int(auxiliary_queue[0]["current_burst"]) == 0 :
					d1["iotime"] = "in"
				else:
					d1["iotime"] = auxiliary_queue[0]["current_burst"]
				if auxiliary_queue[0]["bt"] < auxiliary_queue[0]["time_quantum"] :
					d1["ending_time"] = auxiliary_queue[0]["bt"]
				elif int(auxiliary_queue[0]["current_burst"]) == 0 :
					d1["ending_time"] = auxiliary_queue[0]["time_quantum"]
				elif  auxiliary_queue[0]["bt"] >= auxiliary_queue[0]["time_quantum"] and auxiliary_queue[0]["current_burst"] <= auxiliary_queue[0]["time_quantum"] and auxiliary_queue[0]["current_burst"] != '0' :
					d1["ending_time"] = auxiliary_queue[0]["current_burst"]
				else :
					d1["ending_time"] = auxiliary_queue[0]["time_quantum"]
				del auxiliary_queue[0]
				del auxiliary_list[0]
				list.append(d1)
			current_time = update_auxilaryq(current_time,count)
			update_ready_queue(checkexecution)
	return current_time
#function to print process no and turn around time 
def printfun() :
	print "process name\tturn around time"
	for number in range (0,len(q)) :
		print output[number]["pn"],"	  	    ",output[number]["turn_around"]