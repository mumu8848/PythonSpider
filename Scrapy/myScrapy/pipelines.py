# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pandas as pd
from sqlalchemy import create_engine
from itemadapter import ItemAdapter

class MyscrapyPipeline:
    def __init__(self):
        self.engine = create_engine(
                            'mysql+pymysql://root:123456@127.0.0.1:3306/test',
                            pool_size=10,  # 连接池大小
                            max_overflow=20,  # 连接池最大溢出大小
                            pool_timeout=30,  # 连接池连接超时时间
                            pool_recycle=1800,  # 连接池连接回收时间
                            echo=False  # 打印 SQL 语句，方便调试
                        )

    def process_item(self, item, spider): # self:表示实例对象本身；item:表示接收Items；spider:表示接收Spider
        data = pd.DataFrame(dict(item))
        data.to_sql('tipdm_data',self.engine,if_exists='append',index=False)
        data.to_csv('TipDM_data.csv',mode='a+',index=False,sep='|',header=False)
        return item
