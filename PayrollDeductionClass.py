class PayrollDeduction: 

    def __init__(self, description, date, charge, empID):
        self.__description = description
        self.__date = date
        self.__charge = charge
        self.__empID = empID

    def getDescription(self):
        return self.__description
    
    def getDate(self):
        return self.__date

    def getCharge(self):
        return self.__charge

    def getEmpID(self):
        return self.__empID
        