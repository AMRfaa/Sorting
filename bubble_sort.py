# BUBBLE SORT
data = [64,34,25,30,100,300,1,5,50,20]
print ("data sebelum diurutkan",data)
# i = 20 dan j = 11
banyak_data = len(data)
for i in range (banyak_data-1):
   for j in range (banyak_data-1):
        if data[j] > data[j + 1]:
            temp = data[j]
            data [j] = data [j + 1]
            data [j + 1] = temp
print("data setelah diurutkan",data)
