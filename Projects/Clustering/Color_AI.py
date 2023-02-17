import cv2 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import imutils

clusters = 5 # number of dominant color to show

my_imag = (r'D:\Programming Project\Python Project\AI Project\Color Project\Image.jpeg')
img = cv2.imread(my_imag)
# org_img = img.copy() # make a copy of our image for the futer who is know

print('Org image shape --> ',img.shape) # عرض الحجم الحقيقي للصورة الخاصة بنا 

img = imutils.resize(img,height=200) # تقليل حجم الصورة بشكل يحافظ على شكلها ليك تتم العملية اسرع
print('After resizing shape --> ',img.shape)

flat_img = np.reshape(img,(-1,3)) # عمل اعادة تشكيل للصفوف والاعمدة داخل الصورة بدون تغير البيانات داخل الصورة
print('After Flattening shape --> ',flat_img.shape)

kmeans = KMeans(n_clusters=clusters,random_state=0) # عمل اوبجكت من كيمنز واعطاءه عدد اكثر الاولوان الطاغية
kmeans.fit(flat_img) # وضع الصورة الخاصة بنا في الخوارزمية من بعد ما عملنا لالها فلاتنج او تغير حجم للصورة 

#تحتوي الفلات ايمج على مصفوفة والمصفوفة تحتوي على كل الوان البكسل التي في الصورة بعدها عن طريق الخوارزمية
#  يتم تجميع اكثر الالوان الطاغية في الصورة او اكثر الوان البكسل تكرارا في المصفوفة 
dominant_colors = np.array(kmeans.cluster_centers_,dtype='uint') 

 # يتم حساب نسبة كل لون من الالوان بالنسبة للصورة و وضع النسبة اسفل اللون
percentages = (np.unique(kmeans.labels_,return_counts=True)[1])/flat_img.shape[0] 
#  هذه الجملة ترجع مصفوفة مع جزئين الجزء الاول الجزء الاول الى اي مجموعة ينتمي البكسل
# ويحتوي الجزء الثاني على مجموعة من الارقام يتم قسمتها على 1000 لكي نخرج النسبو الصحيحة للون في كل الصورة
p_and_c = zip(percentages,dominant_colors) # يتم دمج نسبة المئوية الخاص بكل لون مع بعضه البعض
p_and_c = sorted(p_and_c,reverse=True) # يتم تخزين اللون ونسبته ويكون اول عنصر هو الاكثر سيطرة وأعلى نسبة

#======================================================== طريقة عرض اضافية ك مربعات 
block = np.ones((50,50,3),dtype='uint')
plt.figure(figsize=(12,8))
for i in range(clusters):
    plt.subplot(1,clusters,i+1)
    block[:] = p_and_c[i][1][::-1] # we have done this to convert bgr(opencv) to rgb(matplotlib) 
    plt.imshow(block)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel(str(round(p_and_c[i][0]*100,2))+'%')
#======================================================== طريقة عرض اضافية ك شريط او بار 
bar = np.ones((50,500,3),dtype='uint')
plt.figure(figsize=(12,8))
plt.title('Proportions of colors in the image')
start = 0
i = 1
for p,c in p_and_c:
    end = start+int(p*bar.shape[1])
    if i==clusters:
        bar[:,start:] = c[::-1]
    else:
        bar[:,start:end] = c[::-1]
    start = end
    i+=1
plt.imshow(bar)
plt.xticks([])
plt.yticks([])

rows = 1000
cols = int((org_img.shape[0]/org_img.shape[1])*rows) # ارجاع الصورة الى حجمها الاصلي بعد ضربها بعدد الصفوف لكي يتم عرضها للمستخدم
img = cv2.resize(org_img,dsize=(rows,cols),interpolation=cv2.INTER_LINEAR)

copy = img.copy()
cv2.rectangle(copy,(rows//2-250,cols//2-90),(rows//2+250,cols//2+110),(255,255,255),-1) # عرض الاولوان المهيمنة كمربعات في منتصف الصورة الاصلية 

final = cv2.addWeighted(img,0.1,copy,0.9,0)
cv2.putText(final,'Most Dominant Colors in the Image',(rows//2-230,cols//2-40),cv2.FONT_HERSHEY_DUPLEX,0.8,(0,0,0),1,cv2.LINE_AA) # ترتيت الاولوان المهينة من أكثر لون مهين برقم واحد الى الاقل

# تزبيط مكان المربعات في الشاشة والارقام جعل مربعات الالوان في نصف الشاشة والصورة تكون بشكل منانسق مع حجم النافذة
start = rows//2-220
for i in range(5):
    end = start+70
    final[cols//2:cols//2+70,start:end] = p_and_c[i][1]
    cv2.putText(final,str(i+1),(start+25,cols//2+45),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),1,cv2.LINE_AA)
    start = end+20
    
plt.show()
cv2.imshow('img',final)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output.png',final)