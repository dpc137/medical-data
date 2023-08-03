import redis
import csv
import time
class csv_to_redis():
  def __init__(self,host_id,port_id,filename):
      self.host_id=host_id
      self.port_id=port_id
      self.filename=filename
      pass
  def write_csv_to_redis(self):
    r=redis.Redis(host=self.host_id,port=self.port_id)
    with open(self.filename,encoding="gbk") as f:
        reader = csv.DictReader(f)
        times=time.time()
        #遍历读取每一行的数据，并将其作为哈希映射存储到Redis中
        for row in reader:
          ## 读取数据行中的各个字段
          Pregnancies = row["Pregnancies"]
          Glucose = row["Glucose"]
          BloodPressure = row["BloodPressure"]
          SkinThickness= row["SkinThickness"]
          Insulin = row["Insulin"]
          BMI=row["BMI"]
          DiabetesPedigreeFunction=row["DiabetesPedigreeFunction"]
          Age=row["Age"]
          Outcome=row["Outcome"]
          #将字段数据作为哈希表存储到Redis中
          r.hmset(times,{
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI"   :BMI,
        "DiabetesPedigreeFunction":DiabetesPedigreeFunction,
        "Age":Age,
        "Outcome":Outcome
       })
        print(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome)
    f.close()



