import time
def data_read():
	c1=0
	line=f.readline().split()
	while line:
		c1=c1+1	
		dict = {}
		dict[line[-6]]=line[-5]
		dict[line[-4]]=line[-3]
		dict[line[-2]]=line[-1]
		di.append(d)
		line=f.readline().split()
	return c1

def print_func():
	v=0
	print "Process   Turn Around Time   Waiting Time"
	while v<count:
		print process[v],"		",turn_arround[v],"		", wait_time[v]
		v=v+1

if __name__ == "__main__" :
	f=open('file.txt')
	i=0
	t=0
	st=0
	j=0
	k=0
	count =0
	di=[]
	process = []
	count=data_read()
	turn_around = []
	wait_time = []
	nlist=sorted(di, key = lambda k: k['at'])	
	while i<count:

		print di[i]["pn"] ,"Execution Started"
		j=int(di[i]["bt"])
		print di[i]["pn"] ," is going to execute for ", j, "seconds"
		while j>0:
			time.sleep(1)
			j=j-1
			t=t+1
		"""while k<i :
			t=t+int(di[k]["bt"])
			k=k+1"""
		print(di[i]["pn"]), "execution completed."
		turn_ar.append((st+int(di[i]["bt"]))-int(di[i]["at"]))
		wait.append((st-int(di[i]["at"])))
		proc.append(di[i]["pn"])
		i=i+1
		st=t
	print_func()
