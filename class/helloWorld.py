import datetime

class HelloWorld():
  def __init__(self):
    self.nome = input("Oie! Digite seu nome: ")
    self.nascimento = input(f"{self.nome}, digite sua data de nascimento: [dia/mês/ano] ")

  def normalize_date(self, birthday):
    year = birthday[6:]
    month = birthday[3:5]
    day = birthday[:2]

    return year, month, day

  def age(self):
    date = self.normalize_date(self.nascimento)
    ano_nasc, mes_nasc, dia_nasc = int(date[0]), int(date[1]), int(date[2])  

    datetime_now = self.get_datetime()

    dia_atual = datetime_now[2]
    mes_atual = datetime_now[1]
    ano_atual = datetime_now[0]

    idade = ano_atual - ano_nasc

    if mes_atual >= mes_nasc:
      if dia_atual > dia_nasc:
        return f"Você tem {idade} anos!"
      elif dia_atual == dia_nasc and mes_atual == mes_nasc:
        return f"Parabéns, {self.nome}! Hoje você completa {idade} anos!"
      else:
        idade = idade - 1
        return f"Você tem {idade} anos!"
    else:
        idade = idade - 1
        return f"Você tem {idade} anos!"

  def salutations(self):
    hora = self.get_datetime()[-1]

    if hora >= 5 and hora < 12:
      return f"Bom dia, {self.nome}!"
    elif hora >= 12 and hora < 18:
      return f"Boa tarde, {self.nome}!"
    else:
      return f"Boa noite, {self.nome}!"

  def get_datetime(self):
    data_hora_atual = datetime.datetime.utcnow()
    fuso_horario = datetime.timedelta(hours=3)
    data_hora = data_hora_atual - fuso_horario
    data_hora = data_hora.strftime("%d/%m/%Y %H:%M:%S")

    data = data_hora[:11]
    date = self.normalize_date(data)

    ano_atual, mes_atual, dia_atual = int(date[0]), int(date[1]), int(date[2])
    hora = int(data_hora[11:][:2])

    return ano_atual, mes_atual, dia_atual, hora

hello = HelloWorld()
print(hello.salutations())
print(hello.age())