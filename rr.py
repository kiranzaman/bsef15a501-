import time
def data_read():
	f=open('file1.txt')
	line=f.readline().split()
	while line:
		d={}
		d[line[-12]]=line[-11]
		d[line[-10]]=line[-9]
		d[line[-8]]=line[-7]
		d[line[-6]]=line[-5]
		d[line[-4]]=line[-3]
		d[line[-2]]=line[-1]
		di.append(d)
		line=f.readline().split()
	f.close()
def inWaitingq(pname):
	for i in range(0,len(wq)):
		if(wq[i]["pn"] == pname) :
			return True
	return False
def inreadyq(pname):
	for i in range(0,len(rq)):
		if(rq[i]["pn"] == pname) :
			return True
	return False
def find_min() :
	minv = int(wli[0]["rt"])
	ind = 0
	for n in range(0,len(wli)):
		if int(wli[n]["rt"]) < minv:
			minv = int(wli[n]["rt"])
			ind = n
	return ind	
def update_readyq(check):
	j=0
	d = {'ext':0,'et':0,'iot':0}
	for i in range(0,len(q)):
		if int(q[i]["bt"]) > 0 and inWaitingq(q[i]["pn"]) == False and int(q[i]["at"]) <= current_time and inreadyq(q[i]["pn"]) == False :
			rq.append(q[i])
			d["ext"] = q[i]["tq"]
			if int(q[i]["cb"]) == 0 :
				d["iot"] = "in"
			else:
				d["iot"] = q[i]["cb"]
			if q[i]["bt"] < q[i]["tq"] :
				d["et"] = q[i]["bt"]
			elif int(q[i]["cb"]) == 0 :
				d["et"] = q[i]["tq"]
			elif  q[i]["bt"] >= q[i]["tq"] and q[i]["cb"] <= q[i]["tq"] and q[i]["cb"] != '0' :
				d["et"] = q[i]["cb"]
			else :
				d["et"] = q[i]["tq"]
			li.append(d)
		#print li
	d = {'ext':0,'et':0,'iot':0}
	for j in range(0,len(wli)) :
		val = find_min()
		if wli[val]["rt"] <= current_time :
			d["ext"] = wli[val]["ext"]
			d["iot"] = wq[val]["cb"]
			if wli[val]["ext"] < wq[val]["cb"] :
				d["et"] = wli[val]["ext"]
			else :
				d["et"] = wq[val]["cb"]
			#lrt.append(wli[val]["rt"])
			li.append(d)
			rq.append(wq[val])
			print wq[val]["pn"], " is now returning from waiting queue at ", wli[val]["rt"]
			del wq[val]
			del wli[val]
	if check == True :
		rq.append(rq[0])
		li.append(li[0])
		del rq[0]
		del li[0]
	#print li[0]		
def update_waitingq():
	wq.append(rq[0])
	d = {'pn':0,'rt':0,'ext':0}
	d["rt"] = int(rq[0]["ib"])+current_time
	d["ext"] = li[0]["ext"]
	wli.append(d)
def printfun() :
	print "process name	turn around time"
	for a in range (0,len(q)) :
		print output[a]["pn"],"	  	    ",output[a]["ta"]
if __name__ == "__main__" :
	di = []
	q = []
	rq = []
	li = []
	wq = []
	wli = []
	chk = True
	current_time = 0
	output = []
	data_read()
	print di
	#print len(di)
	q = sorted(di, key = lambda k: int(k["at"]))
	update_readyq(False)
	count = 0
	while count != len(q) :
		if len(rq) != 0 :
			if li[0]["et"] != '0' :
				print rq[0]["pn"], " execution started for ",li[0]["et"], "sec at time ", current_time
			var = 0
			while var != int(li[0]["et"]) :
				current_time = current_time +1
				update_readyq(False)
				var = var+1
			li[0]["ext"] = str(int(li[0]["ext"])-int(li[0]["et"]))
			
			if int(li[0]["ext"]) == 0 and li[0]["iot"] > '0' :	
				li[0]["ext"] = rq[0]["tq"]
			if li[0]["iot"] != 'in':
				#print li[0]["iot"], li[0]["et"]
				li[0]["iot"] = str(int(li[0]["iot"])-int(li[0]["et"]))
			rq[0]["bt"] = str(int(rq[0]["bt"])-int(li[0]["et"]))
			if li[0]["iot"] <= li[0]["ext"] and li[0]["iot"] != "in" :
				li[0]["et"] = li[0]["iot"]
			elif li[0]["ext"] <= rq[0]["cb"] :
				li[0]["et"] = li[0]["ext"]
			elif rq[0]["bt"] <= li[0]["ext"] :
				li[0]["et"] = rq[0]["bt"]
			else :
				li[0]["et"] = rq[0]["cb"]
			chk =  True
			#print rq
			#print li[0]
			if int(rq[0]["cb"]) != 0 and int(rq[0]["bt"]) > 0 and li[0]["iot"] == '0' :
				print rq[0]["pn"], " going to waiting queue for ", rq[0]["ib"], "sec at time ", current_time
				chk = False
				update_waitingq()
				del rq[0]
				del li[0]
			if chk == True and int(rq[0]["bt"]) <= 0 :
				print rq[0]["pn"], "execution completed" 
				out_dic = {'pn':0,'ta':0}
				out_dic['ta'] = (current_time-int(rq[0]["at"]))
				out_dic['pn'] = rq[0]["pn"]
				output.append(out_dic)
				count = count + 1
				del rq[0]
				del li[0]
				chk =  False
			update_readyq(chk)
			while len(rq) == 0 and len(q) != count :
				#print "check:",f
				current_time=current_time+1
				update_readyq(False)
		while len(rq) == 0 and len(q) != count :
				#print "check:",f
				update_readyq(False)
				current_time=current_time+1
	printfun()
