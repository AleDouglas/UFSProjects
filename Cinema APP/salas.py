class Salas:
    def __init__(self):
        self.sala_1 = [
            "14:30//17:30//20:30==14:40//17:40//20:40==14:50//17:50//20:50==14:20//17:20//20:20==14:00//17:00//20:00",
            "18:20==18:10==18:40==18:50==18:00",
            "19:00==19:30==19:20==19:15==19:10",
            "10:00//15:50==10:20//15:30==10:10//15:40==10:30//15:20==10:40//15:35",
            "8:00//11:30//13:00==8:10//11:20//13:30==8:40//11:50//13:20==8:30//11:10//13:20==8:15//11:45//13:55",
            "6:00==6:30==6:40==6:15==6:35",

        ]
        self.sala_2 = [
            "18:20==18:10==18:40==18:50==18:00",
            "14:30//17:30//20:30==14:40//17:40//20:40==14:50//17:50//20:50==14:20//17:20//20:20==14:00//17:00//20:00",
            "10:00//15:50==10:20//15:30==10:10//15:40==10:30//15:20==10:40//15:35",
            "19:00==19:30==19:20==19:15==19:10",
            "6:00==6:30==6:40==6:15==6:35",
            "8:00//11:30//13:00==8:10//11:20//13:30==8:40//11:50//13:20==8:30//11:10//13:20==8:15//11:45//13:55",
        ]
        self.sala_3 = [
            "19:00==19:30==19:20==19:15==19:10",
            "10:00//15:50==10:20//15:30==10:10//15:40==10:30//15:20==10:40//15:35",
            "18:20==18:10==18:40==18:50==18:00",
            "14:30//17:30//20:30==14:40//17:40//20:40==14:50//17:50//20:50==14:20//17:20//20:20==14:00//17:00//20:00",
            "9:00//12:30//14:00==9:10//12:20//14:30==9:40//12:50//14:20==9:30//12:10//14:20==9:15//12:45//14:55",
            "7:00==7:30==7:40==7:15==7:35",

        ]
        self.sala_4 = [
            "10:00//15:50==10:20//15:30==10:10//15:40==10:30//15:20==10:40//15:35",
            "8:00//11:30//13:00==8:10//11:20//13:30==8:40//11:50//13:20==8:30//11:10//13:20==8:15//11:45//13:55",
            "14:30//17:30//20:30==14:40//17:40//20:40==14:50//17:50//20:50==14:20//17:20//20:20==14:00//17:00//20:00",
            "18:20==18:10==18:40==18:50==18:00",
            "19:00==19:30==19:20==19:15==19:10",
            "1:00==1:30==1:40==1:15==1:35",

        ]
        self.sala_5 = [
            "8:00//11:30//13:00==8:10//11:20//13:30==8:40//11:50//13:20==8:30//11:10//13:20==8:15//11:45//13:55",
            "19:00==19:30==19:20==19:15==19:10",
            "7:00==7:30==7:40==7:15==7:35",
            "00:20==00:10==00:40==00:50==00:00",
            "10:00//15:50==10:20//15:30==10:10//15:40==10:30//15:20==10:40//15:35",
            "14:30//17:30//20:30==14:40//17:40//20:40==14:50//17:50//20:50==14:20//17:20//20:20==14:00//17:00//20:00",

        ]
        self.lugaresComprados = []

    def lugares(self, listDados):
        self.lugaresComprados.append(listDados)

    def removeLugar(self, listDados):
        self.lugaresComprados.remove(listDados)

    def verificarLugar(self, listDados):
        existe = False
        for i in range(len(self.lugaresComprados)):
            if listDados[0] == self.lugaresComprados[i][0]: #VERIFICANDO NOME DO FILME
                if listDados[1] == self.lugaresComprados[i][1]: #VERIFICANDO SALA
                    if listDados[2] == self.lugaresComprados[i][2]: #VERIFICANDO HORÁRIO
                        if listDados[3] == self.lugaresComprados[i][3]: #VERIFICANDO DIA
                            for x in self.lugaresComprados[i][4]: #VERFICIANDO CADEIRAS
                                for y in listDados[4]:
                                    if x == y:
                                        existe = True
                                        return True
        if existe == False:
            return False

    def changeLugares(self, listDados):
        list = []
        for i in range(len(self.lugaresComprados)):
            if listDados[0] == self.lugaresComprados[i][0]: #VERIFICANDO NOME DO FILME
                if listDados[1] == self.lugaresComprados[i][1]: #VERIFICANDO SALA
                    if listDados[2] == self.lugaresComprados[i][2]: #VERIFICANDO HORÁRIO
                        if listDados[3] == self.lugaresComprados[i][3]: #VERIFICANDO DIA
                            list.append(self.lugaresComprados[i][4])

        return list

    def getSala1(self):
        return self.sala_1
    def getSala2(self):
        return self.sala_2
    def getSala3(self):
        return self.sala_3
    def getSala4(self):
        return self.sala_4
    def getSala5(self):
        return self.sala_5

    def getLugaresComprados(self):
        return self.lugaresComprados

salas = Salas()
#salas.verificarLugar(['Batman', 2, '18:20', 0, ['a1','a2']])