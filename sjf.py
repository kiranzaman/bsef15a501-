import time
def data_read():
	co=0
	line=f.readline().split()
	while line:
		co=co+1	
		d = {}
		d[line[-6]]=line[-5]
		d[line[-4]]=line[-3]
		d[line[-2]]=line[-1]
		di.append(d)
		line=f.readline().split()
	return co
def print_func():
	v=0
	print "process   turn around time   waiting time"
	while v<count:
		print proc[v] ,"		",turn_ar[v],"		", wait[v]
		v=v+1

if __name__ == "__main__" :
	f=open('file.txt')
	i=0
	ct=0
	st=0
	c1=0
	j=0
	ind=0
	k=0
	di =[]
	q=[]
	turn_ar= []
	wait = []
	proc = []
	count=data_read()
	print count
	nlist=sorted(di, key = lambda k: k['bt'])
	while i < count:
		check = False
		q = sorted(nlist, key = lambda k: int(k["bt"]))
		#print q
		j=0
		nlist = q
		while check == False and j<count :
			if (int(q[j]["at"]) < ct or int(q[j]["at"]) == ct):
				ind = j
				check = True
			j=j+1
		tim=int(q[ind]["bt"])
		print(q[ind]["pn"]), "execution started"
		print "now i'm going to execute for ",tim," seconds."
		time.sleep(tim)
		print "execution completed"
		wait.append(ct-int(q[ind]["at"]))
		ct =ct + int(q[ind]["bt"])		
		turn_ar.append(ct-int(q[ind]["at"])) 
		proc.append(q[ind]["pn"])
		nlist[ind]["bt"]=str(100)
		i=i+1
	print_func()
