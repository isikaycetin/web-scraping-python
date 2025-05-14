# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import openpyxl

class BooksPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter['name'] = adapter['name'].upper()
        # sadece stok sayısını aldın

        availability_no = adapter.get('availability').split()[2].split('(')[1]
        adapter['availability'] = availability_no
        # euroları tl ye çevirdik
        converted = float(adapter['price_inc_tax'][1:])*35
        converted_tl = 'Tl' + f'{converted:.2f}'
        adapter['price_inc_tax'] = converted_tl

        return item

class DropperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        availability_no = adapter.get('availability').split()[2].split('(')[1]
        if int(availability_no) >=10:
            adapter['name'] = adapter['name'].upper()
            adapter['availability'] = availability_no
            # euroları tl ye çevirdik
            converted = float(adapter['price_inc_tax'][1:])*35
            converted_tl = 'Tl' + f'{converted:.2f}'
            adapter['price_inc_tax'] = converted_tl

            return item
        else:
            raise DropItem(f'{adapter["name"]} içim yeterli stok yok')


class ExcelPipeline:
    def open_spider(self, spider):
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.sheet.title = 'Books'
        self.sheet.append(['Name','price_exc_tax','price_inc_tax','category','stars', 'upc', 'tax', 'availability', 'image_url'])

    def process_item(self, item, spider):
        self.sheet.append([item.get('name'),
                           item.get('price_exc_tax'),
                           item.get('price_inc_tax'),
                           item.get('category'),
                           item.get('stars'),
                           item.get('upc'),
                           item.get('tax'),
                           item.get('availability'),
                           item.get('image_url')])
        return item

    def close_spider(self, spider):
        self.workbook.save('excelpipelines.xlsx')