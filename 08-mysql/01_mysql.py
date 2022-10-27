from pymysql import connect


class JD(object):
    def __init__(self):
        # 创建Connection连接
        self.conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='123456',
                            charset='utf8')
        # 获得Cursor对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭Cursor对象
        self.cursor.close()
        # 关闭Connection对象
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        """查询所有商品分类"""
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_cates(self):
        """查询所有商品分类"""
        sql = "select name from goods_cates;"
        self.execute_sql(sql)

    def show_bands(self):
        """查询所有的商品品牌分类"""
        sql = "select name from goods_brands;"
        self.execute_sql(sql)

    def add_brands(self):
        item_name = input("请输入商品分类名字：")
        sql = """insert into goods_brands (name) values ("%s")""" % item_name
        self.cursor.execute(sql)
        self.conn.commit()

    @staticmethod
    def print_menu():
        print("-----京东商城-----")
        print("1. 查询所有的商品")
        print("2. 查询所有的商品分类")
        print("3. 查询所有的商品品牌分类")
        print("4. 添加一个商品分类")
        return input("请输入你要查询的数字：")

    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                # 查询所有的商品分类
                self.show_all_items()

            elif num == "2":
                # 查询所有的商品分类
                self.show_cates()

            elif num == "3":
                # 查询所有的商品品牌分类
                self.show_bands()

            elif num == "4":
                # 添加一个商品分类
                self.add_brands()
            else:
                break
                # print("输入有误")


def main():
    # 创建一个京东对象
    jd = JD()
    # 调用run方法
    jd.run()


if __name__ == "__main__":
    main()
