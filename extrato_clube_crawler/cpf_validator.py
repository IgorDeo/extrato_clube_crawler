class CPFValidator:
    @staticmethod
    def is_valid(cpf):
        cpf = CPFValidator.extract_numbers(cpf)
        if len(cpf) != 11:
            return False
        if len(set(cpf)) == 1:
            return False
        dv1 = CPFValidator._calculate_verification_digit(cpf, 10)
        dv2 = CPFValidator._calculate_verification_digit(cpf, 11)
        if cpf[-2:] == str(dv1) + str(dv2):
            return True
        else:
            return False

    @staticmethod
    def _calculate_verification_digit(cpf, weight):
        soma = sum(int(cpf[i]) * (weight - i) for i in range(weight - 1))
        resto = 11 - (soma % 11)
        if resto > 9:
            return 0
        else:
            return resto

    @staticmethod
    def extract_numbers(cpf):
        return "".join(filter(str.isdigit, cpf))
