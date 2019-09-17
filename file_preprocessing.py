import csv 
import re
import sys
nm=""
nt=""
rn=""
pt=""
sp_rn=""
fin=open(sys.argv[1],"rt")
reader=csv.reader(fin)
with open('output.csv', 'wt',newline='') as f:
 fieldname=['number_from','number_to','resource','port_type','sp_rn']
 writer = csv.DictWriter(f,fieldnames=fieldname,delimiter=';')
 writer.writeheader()
 for row in reader:
  for i in range(len(row)):
   if re.search('^ent_sub\(dn',row[i]):
    nm=row[i].replace("ent_sub(dn ","")
    nt=""
   if re.search('^ent_sub\(bdn',row[i]):
    nm=row[i].replace("ent_sub(bdn ","")
    nt=row[i+1].replace("edn ","")
   if re.search('pt',row[i]):
    pt=row[i].replace("pt ","")
   if re.search('rn',row[i]):
    rn=row[i].replace("rn ","")
    sp_rn="rn"
   if re.search('sp',row[i]):
    rn=row[i].replace("sp ","")
    sp_rn="sp"
   if re.search('\)',pt):
    pt=pt.replace(")","")
   if re.search('\)',rn):
    rn=rn.replace(")","")
   nm=nm.strip()
   nt=nt.strip()
   rn=rn.lstrip()
   pt=pt.lstrip()
   sp_rn=sp_rn.strip()
  writer.writerow({'number_from': nm,'number_to':nt,'resource':rn,'port_type':pt,'sp_rn':sp_rn})
