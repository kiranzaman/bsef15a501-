import time
def data_read(li):
	f=open('file.txt')
	co=0
	line=f.readline().split()
	while line:
		co=co+1	
		d = {}
		d[line[-6]]=line[-5]
		d[line[-4]]=line[-3]
		d[line[-2]]=line[-1]
		li.append(d)
		line=f.readline().split()
	f.close()
	return co
def check_job(val):
	j=0
	ind=0
	check=False
	while check == False and j<count :
			if (int(q[j]["at"]) < val or int(q[j]["at"]) == val):
				ind = j
				check = True
			j=j+1
	return ind
def search_at(pn):
	n=0
	rt=0
	while n<count :
		if pn == di[n]["pn"] :
			rt=int(di[n]["at"])
		n=n+1
	return rt
	
def search_bt(pn1):
	m=0
	rt1=0
	while m<count :
		if pn1 == di[m]["pn"] :
			rt1=int(di[m]["bt"])
		m=m+1
	return rt1
def print_func():
	v=0
	print "process   turn around time   waiting time"
	while v<count:
		print proc[v] ,"		",turn_ar[v],"		", wait[v]
		v=v+1

if __name__ == "__main__" :

	i=0
	wt=0
	index=0
	kind=0
	k=0
	di =[]
	q=[]
	nlist=[]
	chk=True
	count=data_read(di)
	data_read(nlist)
	turn_ar=[]
	wait=[]
	proc=[]
	while chk== True:
		chk=False
		q = sorted(nlist, key = lambda k: int(k["bt"]))
		nlist = q
		index=check_job(k)
		kind=index
		print(q[index]["pn"]), "execution started"
#		print "now i'm going to sleep for ",tim," seconds."
		while kind == index and int(q[index]["bt"]) >0:
			time.sleep(1)
			k=k+1
			val=int(q[index]["bt"])
			val=val-1
			q[index]["bt"]=str(val)
			kind = check_job(k)

		if int(q[index]["bt"]) > 0:
			print q[index]["pn"], "execution stopped"
		else:
			print q[index]["pn"], "execution completed"
			
			wait.append(k-search_at(q[index]["pn"])-search_bt(q[index]["pn"]))
	
			turn_ar.append(k-search_at(q[index]["pn"]))
			proc.append(q[index]["pn"])
			nlist[index]["bt"]=str(1000)
		n=0
		while n<count :
			if int(nlist[n]["bt"])!=1000:
				chk=True
			n=n+1
	print_func()
