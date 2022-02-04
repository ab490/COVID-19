#Name: Anooshka Bajaj

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel(r'E:\Covid19IndiaData_.xlsx')

#1(i)
ages={}
n=len(df)
for i in df['Age']:
    try:
        ages[i]+=(1/n)
    except:
        ages.update({i:1/n})

fig,ax=plt.subplots()
ax.set_yscale('log')
ax.stem(ages.keys(),ages.values(),use_line_collection=True)

ex=0
ex2=0
for i,j in ages.items():
    ex+=(i*j)
    ex2+=(i*i*j)
var=ex2-ex**2
print(ex,var)

#The variance is high. This implies that a wide
#range of age groups are affected. Max no. is around 38

#1(ii)
aged={}
ager={}
for i in range(n):
    if df.loc[i]['StatusCode']=='Dead':
        try:
            aged[df.loc[i]['Age']]+=1
        except KeyError:
            aged.update({df.loc[i]['Age']:1})
    else:
        try:
            ager[df.loc[i]['Age']]+=1
        except KeyError:
            ager.update({df.loc[i]['Age']:1})

rc=sum(ager.values())
dc=sum(aged.values())
fig,ax=plt.subplots(1,2,figsize=(15,5))
ax[0].set_yscale('log')
ax[0].set_title('Recovered')
ax[0].stem(ager.keys(),np.array(list(ager.values()))/rc,use_line_collection=True)
ax[1].set_yscale('log')
ax[1].set_title('Dead')
ax[1].stem(aged.keys(),np.array(list(aged.values()))/dc,use_line_collection=True)

exr=0
ex2r=0
for i,j in ager.items():
    exr+=(i*j/rc)
    ex2r+=(i*i*j/rc)
varr=ex2r-exr**2
print(exr,varr)

exd=0
ex2d=0
for i,j in aged.items():
    exd+=(i*j/dc)
    ex2d+=(i*i*j/dc)
vard=ex2d-exd**2
print(exd,vard)

#From the expectation values, we can say that COVID is more dangerous for
# elder people

#1(iii)
agem={}
agef={}
for i in range(n):
    if df.loc[i]['GenderCode0F1M']==0:
        try:
            agef[df.loc[i]['Age']]+=1
        except:
            agef.update({df.loc[i]['Age']:1})
    else:
        try:
            agem[df.loc[i]['Age']]+=1
        except:
            agem.update({df.loc[i]['Age']:1})
            
mc=sum(agem.values())
fc=sum(agef.values())
fig,ax=plt.subplots(1,2,figsize=(15,5))
ax[0].set_title('Male Patients')
ax[0].set_yscale('log')
ax[0].stem(agem.keys(),np.array(list(agem.values()))/mc,use_line_collection=True)
ax[1].set_title('Female Patients')
ax[1].set_yscale('log')
ax[1].stem(agef.keys(),np.array(list(agef.values()))/fc,use_line_collection=True)
plt.show()

exm=0
ex2m=0
for i,j in agem.items():
    exm+=(i*j/mc)
    ex2m+=(i*i*j/mc)
varm=ex2m-exm**2
print(exm,varm)

exf=0
ex2f=0
for i,j in agef.items():
    exf+=(i*j/fc)
    ex2f+=(i*i*j/fc)
varf=ex2f-exf**2
print(exf,varf)

#The expectation values are independant of the gender of the person i.e. it affects males and females equally

# 2(i)
data=pd.read_excel(r'E:\Covid19WorldData_.xlsx',sheet_name=0,header=1)
inc={}

for i,j,k in zip(data['ExposureL'],data['Onset'],data['ExposureType']):
    if k=='Lives-works-studies in Wuhan' and pd.isnull(i):
        i=pd.Timestamp('2019-12-01')
    if not pd.isnull(i) and not pd.isnull(j):
        try:
           inc[int(str(j-i).split()[0])]+=1
        except:
            inc.update({int(str(j-i).split()[0]):1})
            
incv=sum(inc.values())
fig,ax=plt.subplots()
ax.set_yscale('log')
ax.stem(inc.keys(),np.array(list(inc.values()))/incv,use_line_collection=True)

ex=0
ex2=0
for i,j in inc.items():
    ex+=(i*j/incv)
    ex2+=(i*i*j/incv)
var=ex2-ex**2
print(ex,var)

#2(ii)
notwuhan=data[(data['ExposureType']!='Lives-works-studies in Wuhan')]
incnw={}

for i,j in zip(notwuhan['ExposureL'],notwuhan['Onset']):
    if not pd.isnull(i) and not pd.isnull(j):
        try:
           incnw[int(str(j-i).split()[0])]+=1
        except:
            incnw.update({int(str(j-i).split()[0]):1})
            
incnwv=sum(incnw.values())
fig,ax=plt.subplots()
ax.set_yscale('log')
ax.stem(incnw.keys(),np.array(list(incnw.values()))/incnwv,use_line_collection=True)

ex=0
ex2=0
for i,j in incnw.items():
    ex+=(i*j/incnwv)
    ex2+=(i*i*j/incnwv)
var=ex2-ex**2
print(ex,var)

# Wuhan Residents have a longer incubation period as compared to others

#2(iii)
dead=pd.read_excel(r'E:\Sem 2\IC252 Data Science 2\linton_supp_tableS1_S2_8Feb2020.xlsx',sheet_name=1,header=1)
daysho={}

for i in range(len(dead)):
    if not pd.isnull(dead.loc[i]['Hospitalization/Isolation']) and not pd.isnull(dead.loc[i]['Onset']):
        ds=int(str(dead.loc[i]['Hospitalization/Isolation']-dead.loc[i]['Onset']).split()[0])
        try:
            daysho[ds]+=1
        except:
            daysho.update({ds:1})

dc=sum(daysho.values())
fig,ax=plt.subplots()
ax.set_yscale('log')
ax.set_title('Onset - Hospitalization for Dead Patients')
ax.stem(daysho.keys(),np.array(list(daysho.values()))/dc,use_line_collection=True)

ex=0
ex2=0
for i,j in daysho.items():
    ex+=(i*j/dc)
    ex2+=(i*i*j/dc)
var=ex2-ex**2
print(ex,var)

daysdo={}

for i in range(len(dead)):
    if not pd.isnull(dead.loc[i]['Death']) and not pd.isnull(dead.loc[i]['Onset']):
        ds=int(str(dead.loc[i]['Death']-dead.loc[i]['Onset']).split()[0])
        try:
            daysdo[ds]+=1
        except:
            daysdo.update({ds:1})

dc=sum(daysdo.values())
fig,ax=plt.subplots()
ax.set_yscale('log')
ax.set_title('Onset - Death')
ax.stem(daysdo.keys(),np.array(list(daysdo.values()))/dc,use_line_collection=True)

ex=0
ex2=0
for i,j in daysdo.items():
    ex+=(i*j/dc)
    ex2+=(i*i*j/dc)
var=ex2-ex**2
print(ex,var)

dayshd={}

for i in range(len(dead)):
    if not pd.isnull(dead.loc[i]['Hospitalization/Isolation']) and not pd.isnull(dead.loc[i]['Death']):
        ds=int(str(dead.loc[i]['Death']-dead.loc[i]['Hospitalization/Isolation']).split()[0])
        try:
            dayshd[ds]+=1
        except:
            dayshd.update({ds:1})

dc=sum(dayshd.values())
fig,ax=plt.subplots()
ax.set_yscale('log')
ax.set_title('Hospitalization - Death')
ax.stem(dayshd.keys(),np.array(list(dayshd.values()))/dc,use_line_collection=True)

ex=0
ex2=0
for i,j in dayshd.items():
    ex+=(i*j/dc)
    ex2+=(i*i*j/dc)
var=ex2-ex**2
print(ex,var)

# random variable Onset-Death = Onset-Hospitalizaton + Hospitalization-Death

dayshol={}

for i in range(len(data)):
    if not pd.isnull(data.loc[i]['DateHospitalizedIsolated']) and not pd.isnull(data.loc[i]['Onset']):
        ds=int(str(data.loc[i]['DateHospitalizedIsolated']-data.loc[i]['Onset']).split()[0])
        try:
            dayshol[ds]+=1
        except:
            dayshol.update({ds:1})

dcl=sum(dayshol.values())
fig,ax=plt.subplots()
ax.set_yscale('log')
ax.set_title('Onset - Hospitalization for Living Patients')
ax.stem(dayshol.keys(),np.array(list(dayshol.values()))/dcl,use_line_collection=True)

ex=0
ex2=0
for i,j in dayshol.items():
    ex+=(i*j/dcl)
    ex2+=(i*i*j/dcl)
var=ex2-ex**2
print(ex,var)

# Those who survived have lesser expectation of O - H


#3
import math
import matplotlib.pyplot as plt
a=1/57

def pdf(x):
    p=a*math.e**(-a*x)
    return p
def cdf(x):
    c=1-math.e**(-a*x)
    return c

print("(a)")
X=range(500)
Y=[pdf(x) for x in X]

plt.plot(X,Y,linewidth=3,c='green')
plt.xlabel('Time(Hrs)')
plt.ylabel('PDF')
plt.show()

print('(b)    P(Wait time<=1min) = ',cdf(1/60))
print('(c)    P(1min<Wait time<=2min) = ', cdf(2/60)-cdf(1/60))
print('(d)    P(Wait time>2 min) = ', 1-cdf(2/60))

a*=0.5
print('(e)    P(1min<Wait time=<2min) = ', cdf(2/60)-cdf(1/60))

