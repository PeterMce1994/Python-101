class Series :
    seriesHit = 'Most Popular TV Shows'

    def __init__(self,Name,imdb,year):
        self.Name = Name
        self.imdb  = imdb
        self.year = year

    def Drama(self):
        print('แนวชีวิต')
    def Action(self):
        print('แนวบู๊')
    def Adventure(self):
        print('แนวผจญภัย')
    def History(self):
        print('แนวประวัติศาสตร์')

class Rangking(Series) :

    def checkImdb(self):
        if self.imdb >= 9.0:
            print('ห้ามพลาดเด็ดขาด')
        elif self.imdb >=7.0:
            print('ต้องชม')
        else: 
            print('พอชมได้')   

    def checkYear(self):
        if self.year >= 2020:
            print('ซีรีย์เมื่อไม่นานมานี้')
        elif self.year >2010:
            print('ซีรีย์เมื่อประมาณ 10 ปีที่แล้ว')
        else:
            print('ซีรีย์เก่ามากๆ')        
           
print('=================================================')
Series1 = Rangking('Breaking Bad',9.5,2008)
print(f'{Series1.seriesHit}')
print(f'Series:{Series1.Name}')
print(f'IMDB:{Series1.imdb}')
print(f'Year:{Series1.year}')
Series1.checkImdb()
Series1.checkYear()
Series1.Drama()
print('=================================================')
Series2 = Rangking('The Last of Us',9.1,2023)
print(f'Series:{Series2.Name}')
print(f'IMDB:{Series2.imdb}')
print(f'Year:{Series2.year}')
Series2.checkImdb()
Series2.checkYear()
Series2.Drama() 
Series2.Action()
Series2.Adventure()
print('=================================================')
Series3 = Rangking('The Last Kingdom',8.5,2015)
print(f'Series:{Series3.Name}')
print(f'IMDB:{Series3.imdb}')
print(f'Year:{Series3.year}')
Series3.checkImdb()
Series3.checkYear()
Series3.History()
Series3.Drama()
print('=================================================')    
Series4 = Rangking('The Flash',7.5,2014)
print(f'Series:{Series4.Name}')
print(f'IMDB:{Series4.imdb}')
print(f'Year:{Series4.year}')
Series4.checkImdb()
Series4.checkYear()
Series4.Action()
print('=================================================')
Series5 = Rangking('Red Rose',6.4,2022)
print(f'Series:{Series5.Name}')
print(f'IMDB:{Series5.imdb}')
print(f'Year:{Series5.year}')
Series5.checkImdb()
Series5.checkYear()
Series5.Drama()
print('=================================================')
Series6 = Rangking('Sex/Life',5.5,2021)
print(f'Series:{Series6.Name}')
print(f'IMDB:{Series6.imdb}')
print(f'Year:{Series6.year}')
Series6.checkImdb()
Series6.checkYear()
Series6.Drama()

