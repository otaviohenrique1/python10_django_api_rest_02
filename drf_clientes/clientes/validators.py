def validate_cpf(self, cpf):
    if len(cpf) != 11:
        raise serializers.ValidationError("O CPF deve ter 11 dígitos")
    return cpf