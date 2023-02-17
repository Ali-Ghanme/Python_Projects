#Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#importing the dtaset

dataset = pd.read_csv(r"D:\File\Programming Project\Python Project\Machine learning\Simple Liner regrission\Salary_Data.csv")

# determin independent values.
X = dataset.iloc[:,:-1].values # تحديد القيم المستقلة والفصل بينها عن طريق النقطتين الى فوق بعض زي هيك : افهمتو ولا لا

# determin dependent values  train_test_split(X,y,test_size=0.3, random_state=0)
# iloc هي المسؤولة عن فصل البيانات
y =dataset.iloc[:,1].values #spliting the dataset into the training set and test set # (X , Y) تقسيم البيانات الى الى عمودين 

# يتم عمل ثلاث اوبجتكت الاكسترين عشان يدرب المودل على البيانات والاكستست عشان يقيم النتيجة لاى بتطلع من المودل بالبيانات الموجودة وكذالك بعمل مع الوايترين والوايتستت
X_train,X_test, y_train, y_test= train_test_split(X,y,test_size=0.3, random_state=0)

# استخدام خوارزمية اللينر ريجريشن 
regressor = LinearRegression()
# تدريب البيانات باستخدام دالة fit
regressor.fit(X_train,y_train)

# عمل متغير y_pred كنتيجة للتوقع في عمود الواي
y_pred=regressor.predict(X_test)
# عمل توقع التدريب ومقارنتها مع x_traine
y_pred_train=regressor.predict(X_train)

# عرض البيانات بطرق مختلفة عن طريق مكتبة matpliote
plt.scatter(X_train,y_train,color='red') # طريقة لعرض البيانات التي يتم لاتدرب عليها
plt.plot(X_train,y_pred_train,color='blue') # عرض البيانات التي يتم التدرب عليها و نفس البيانات المتوقعة من المودل
plt.title('Salary vs Experience(training set)') # وضع عنوان 
plt.xlabel('years of experience') # وضع عنوان لل x
plt.ylabel('Salary') # وضع عنوان لل y
plt.show() # عرض المخطط الرسومي 

plt.scatter(X_test,y_test,color='red')
plt.plot(X_train,y_pred_train,color='blue')
plt.title('Salary vs Experience(test set)')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()