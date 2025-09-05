# class 참치선물세트:          
#     일반 = 0
#     야채 = 0
#     고추 = 0
#     def 총합(self, 이름):
#         내용물갯수 = self.일반 + self.야채 + self.고추
#         print(이름 + str(내용물갯수) + "개")
#     def 출력(self):
#         self.총합("담긴 참치 갯수 : ")

# 참치1호세트 = 참치선물세트()

# 참치1호세트.일반 = 12
# 참치1호세트.야채 = 3
# 참치1호세트.고추 = 3

# 참치1호세트.출력()

# class Units:
#     hp = 0
#     damage = 0
#     speed = 0

# timo = Units()
# timo.hp = 10
# timo.damage = 100
# timo.speed = 50

# yasuo = Units()
# yasuo.hp = 5
# yasuo.damage = 1000
# yasuo.speed = 100

# print(f'티모 - 체력 : {timo.hp} | 공격력 : {timo.damage} | 이속 : {timo.speed}')

# yasuo.hp -= timo.damage

# print(yasuo.hp)

class 참치선물세트:          
    def __init__(self, 일반, 아채, 고추):
        self.normal = 일반
        self.vege = 아채
        self.pepper = 고추

    def 내용물보기(self, name):
        print(name)
        print("일반참치 : " + str(self.normal))
        print("야채참치 : " + str(self.vege))
        print("고추참치 : " + str(self.pepper))

참치1호세트 = 참치선물세트(10, 3, 2)
참치1호세트.내용물보기("참치1호세트 내용물 안내")