class fatorial:
  def __init__(self,numf):
    self.numf=numf
  def c_fatorial(self):
    if (self.numf == 0):
      return 1

    else:
      resul=1
      for i in range (1,self.numf+1):
        resul*=i
      return resul
f1=fatorial(5)
print(f1.c_fatorial())