#导包
from pyspark import SparkConf, SparkContext
#创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("text")
#基于SparkConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)
#停止Pyspark程序
sc.stop()