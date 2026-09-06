"""和文件相关的类定义"""
import json

from torch.utils.tensorboard import FileWriter

from data_define import Record

class FileReader:

    def read_data(self) -> list[Record]:
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path



    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='utf-8')

        record_list : list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(',')
            record = Record(data_list[0], data_list[1], float(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()

        return record_list



class JsonFileReader(FileWriter):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        record_list = []
        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    data_dict = json.loads(line)
                    record = Record(data_dict["date"], data_dict["order_id"], float(data_dict["money"]),
                                    data_dict["province"])
                    record_list.append(record)
                except json.JSONDecodeError:
                    print(f"跳过格式错误行: {line}")
        return record_list








