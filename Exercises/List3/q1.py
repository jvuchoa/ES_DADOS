class m_Aluno:

  def __init__ (self, n1,n2,n3,n4,n5):
    self.n1=n1
    self.n2=n2
    self.n3=n3
    self.n4=n4
    self.n5=n5

  def aprovacao(self):
    total=(self.n1 +self.n2 +self.n3 +self.n4 +self.n5 )/5
    if (total>=7):
      return f"O aluno foi aprovado com média: {total}"
    else:
      return f"O aluno foi reprovado com média: {total}"
m1=m_Aluno(6,7,8,6,1)
print(m1.aprovacao())
