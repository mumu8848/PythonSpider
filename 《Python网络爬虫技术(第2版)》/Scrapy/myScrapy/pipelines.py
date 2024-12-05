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
        self.engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test')

    def process_item(self, item, spider):
        # 将 item 转换为 DataFrame
        data = pd.DataFrame([dict(item)])

        # 将数据写入 MySQL 数据库
        try:
            data.to_sql('tipdm_data', self.engine, if_exists='append', index=False)
        except Exception as e:
            print(f"Error writing to MySQL: {e}")

        # 将数据追加到 CSV 文件
        try:
            data.to_csv('TipDM_data.csv', mode='a+', index=False, sep='|', header=False)
        except Exception as e:
            print(f"Error writing to CSV: {e}")

        return item
