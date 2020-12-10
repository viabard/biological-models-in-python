import os

os.chdir("D:\\SCHOOL\\fall 2020\\Biological Models in Python\\Week 8")

class dataset:
    def __init__(self, fileName):
        fileThing = open(fileName, "r")
        self.numbers = fileThing.readlines()
        fileThing.close()

    def Calcmean(self):
        s = 0
        for number in self.numbers:
            s += float(number.strip("\n"))
        return s/len(self.numbers)

    def Calcvariance(self):
        s = self.Calcmean()
        s2 = 0
        for i in self.numbers: 
            s2 += pow((float(i) - s), 2) 
        return (s2/(len(self.numbers) - 1))

x = dataset("datafile.txt")
print(x.Calcmean())
print(x.Calcvariance())