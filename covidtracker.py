#Covid Tracker 
#Internet Connection is must !!
from covid import Covid
import covid
import matplotlib.pyplot as plt


covid = Covid()
name = input("Enter the name of the country : ")

virusdata = covid.get_status_by_country_name(name)

#remove residual data
remove = ['id','country','latitude','longitude','last_update']
for i in remove:
    virusdata.pop(i)
all = virusdata.pop('confirmed')
#print(virusdata)

id = list(virusdata.keys())
value = [str(i) for i in virusdata.values()]

plt.pie(value, labels=id, colors= ['r','y','g','b'], autopct= '%1.1f%%')
plt.title("COUNTRY : "+name.upper() +"\n TOTAL CASES : "+str(all))
plt.legend()
plt.show()