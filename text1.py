from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = 'C:\\Users\\YAO\\PycharmProjects\\PythonProject\\pyspark\\text1.py'
os.environ['HADOOP_HOME'] = '"D:\\hadoop-3.0.0"'
conf = SparkConf().setMaster("local[*]").setAppName("text")
sc = SparkContext(conf=conf)

file_rdd = sc.textFile("file:///SparkCourse/sample.txt")
#将数据按制表符切分，取x[0]列，并取前两位数字，设为key，value设为1，分组聚合后，按x[1]进行排序，取前三个
resulr1 = file_rdd.map(lambda x:((x.split("\t")[0][:2]),1)).\
    reduceByKey(lambda x,y:x+y).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3)
print(resulr1)


