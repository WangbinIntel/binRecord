import pandas as pd
from decimal import Decimal

class Lottery:
    def __init__(self, luckNum, filePath):
        self.luckNum = luckNum
        self.filePath = filePath

    def sub_luckNum(self, num):
        return abs(Decimal(num) - self.luckNum)

    def read_data(self):
        file_data = pd.read_excel(self.filePath)
        return pd.DataFrame(file_data, columns=['E-mail', 'Number'])

    def run(self):
        data = self.read_data()
        print(data)
        print()
        data['Num_modified'] = data['Number'].map(self.sub_luckNum)
        data = data.sort_values(by='Num_modified', ascending=True)
        data.to_excel('/Users/wangbin/Desktop/jd12.xlsx')


if __name__ == '__main__':
    luckNum = 627
    ll = Lottery(luckNum, '/Users/wangbin/Desktop/jd1.xlsx')
    ll.run()
