import csv
import time
import  math
import random
#定义生成数据写入csv的代码
class data_into_csv():
  def __init__(self,filename):
      self.filename=filename
      pass
  def write_data_into_csv(self):
    with open(self.filename, 'w', newline='') as csvfile:
      fieldnames = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']
      #写入CSV文件，并按行将字典的键值对写入文件中的每一列
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      #清空数据
      csvfile.truncate()
      #标题行
      writer.writeheader()
      # 获取当前时间的时间戳
      timestamp = time.time()
      # 将时间戳转换为一个周期为30秒的值域在[0, 2π]之间的小数
      theta = (timestamp % 60) / 60 * 2 * math.pi
      #讲
      Pregnancies = round(20 * abs(math.sin(theta)) + 10, 2)
      glucose=round(200 * abs(math.sin(theta)) + 10, 2)
      bloodpressure=round(100 * abs(math.sin(theta)) + 100, 2)
      skinthickness=round(40 * abs(math.sin(theta)) + 10, 2)
      insulin=round(1000 * abs(math.sin(theta)), 2)
      bmi=round(25  * abs(math.sin(theta)) + 10, 2)
      diabetespediigreefunction=round(2 * abs(math.sin(theta)), 2)
      age=round(80 * abs(math.sin(theta)) , 0)
      outcome=random.choice([0,1])
      writer.writerow({'Pregnancies': Pregnancies,'Glucose':glucose,'BloodPressure':bloodpressure,'SkinThickness':skinthickness,'Insulin':insulin,'BMI':bmi,'DiabetesPedigreeFunction':diabetespediigreefunction,'Age':age,'Outcome':outcome})
      #确保所有的数据都被写入到文件
      csvfile.flush()
    csvfile.close()

