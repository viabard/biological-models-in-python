

class dataset():

    def __init__(self,filename):
        self.vals = []

##        vals2 = []
        with open(filename,'r') as fp:
            for line in fp:
                self.vals.append(float(line))
##                vals2.append(float(line))
        fp.close()

    def __len__(self):
        return len(self.vals)

##    def len(self):
##        return len(self.vals)

    def calcmean(self):
        sum = 0.0
        for v in self.vals:
            sum += v
        return sum/len(self.vals)

    def calcvariance(self):
        sum = 0.0
        sumsq = 0.0
        for v in self.vals:
            sum += v
            sumsq += v*v
        n = len(self.vals)
        variance = (sumsq - pow(sum,2)/float(n))/float(n-1)
        return variance



a = dataset("datafile.txt")
print (len(a),a.calcmean(),a.calcvariance())