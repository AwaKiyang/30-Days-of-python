age = [31,26,34,37,27,26,32,32,26,27,27,24,32,33,27,25,26,38,37,31,34,24,33,29,26]
class statistics:
    def __init__(self,age_data):
        self.age_data =age_data
    def count(self):
        return len(self.age_data)
    def total(self):
        return sum(self.age_data)
    def minimum(self):
        return min(self.age_data)
    def maximum(self):
        return max(self.age_data)

data = statistics(age)
print('count : ', data.count())
print('Sum : ', data.total())
print('Min : ', data.minimum())
print('Maximum : ', data.maximum())

