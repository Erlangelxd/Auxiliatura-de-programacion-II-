# Defina la clase Número Real y establezca métodos para:
# a) Invertir el número
# b) Encontrar el dígito mayor
# c) Desplegar la cantidad de dígitos primos
# d) Eliminar el i-ésimo dígito
class Numero_real:
    def __init__(self, numero):
        self.numero=numero
    def invertir_numero(self):
        num=str(self.numero)
        return f"Inversa: {num[::-1]}"
    def digito_mayor(self):
        num=str(self.numero)
        return f"El digito mayor es: {max(num)} "
    def primos(self):
        def generador(valor):
            if valor <= 1:
                return False
            for i in range(2, int(valor ** 0.5) + 1):
                if valor % i == 0:
                    return False
            return True
        num2=[]
        num=str(self.numero)
        for digito in num:
            if generador(int(digito)):
                num2.append(digito)
        return f"La cantidad de digitos primos es: {len(num2)}"
    def eliminar_posicion(self, posicion):
        V=[]
        num=str(self.numero)
        for digito in num:
            V.append(int(digito))
        V.pop(posicion-1)
        return(f"Se eliminó la posicion: {posicion} quedando: {V}")


numero=Numero_real(123456789)
print(numero.invertir_numero())
print(numero.digito_mayor())
print(numero.primos())
print(numero.eliminar_posicion(7))
