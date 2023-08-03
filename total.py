import csv,time,redis,math,random
from csv_to_redis import  csv_to_redis
from write_into_csv import data_into_csv
if __name__=='__main__':
  filename = "D:\\output.csv"
  host_id = "127.0.0.1"
  port_id = "6379"
  data_into_csv_instance = data_into_csv(filename)
  csv_to_redis_instance=csv_to_redis(host_id,port_id,filename)
  while True:
        data_into_csv_instance.write_data_into_csv()
        print("新数据已导入csv")
        csv_to_redis_instance.write_csv_to_redis()
        print("新数据已导入redis")
        time.sleep(1)
