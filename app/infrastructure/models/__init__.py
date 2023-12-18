from django.db import models


class DadosGestante(models.Model):
    # DADOS DA GESTANTE
    numero_cartao_sus = models.CharField(max_length=20)
    numero_nis = models.CharField(max_length=20)
    nome = models.CharField(max_length=255)
    apelido = models.CharField(max_length=255)
    nome_companheiro = models.CharField(max_length=255, blank=True, null=True)
    data_nascimento = models.DateField()
    idade = models.IntegerField()
    raca_cor = models.CharField(max_length=20)
    etnia = models.CharField(max_length=20)
    trabalha_fora_casa = models.BooleanField()
    ocupacao = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    ponto_referencia = models.CharField(max_length=255)
    indigena_dsei = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    cep = models.CharField(max_length=10)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    emergencia_nome = models.CharField(max_length=255)
    emergencia_telefone = models.CharField(max_length=20)
    emergencia_companheiro = models.BooleanField()
    emergencia_familiar_amigo = models.BooleanField()
    emergencia_outros = models.BooleanField()

    # Importantes para a consulta clínica
    escolaridade = models.CharField(max_length=255)
    peso_anterior_kg = models.FloatField()
    altura_cm = models.FloatField()
    estado_civil = models.CharField(max_length=255)
    dum_data = models.DateField()
    dpp_data = models.DateField()
    dpp_eco_data = models.DateField()
    tipo_gravidez = models.CharField(
        max_length=255,
        choices=[
            ("unica", "Única"),
            ("gemelar", "Gemelar"),
            ("tripla_ou_mais", "Tripla ou Mais"),
            ("ignorada", "Ignorada"),
        ],
    )
    risco = models.CharField(
        max_length=255, choices=[("habitual", "Habitual"), ("alto_risco", "Alto Risco")]
    )
    gravidez_planejada = models.BooleanField()
    antecedentes_familiares = models.TextField()
    antecedentes_clinicos_obstetricos = models.TextField()
    gestacao_atual = models.TextField()


class GanhoPeso(models.Model):
    gestante = models.ForeignKey(DadosGestante, on_delete=models.CASCADE)
    altura = models.FloatField()
    peso = models.FloatField()
    imc = models.CharField(max_length=20)


class AlturaUterina(models.Model):
    gestante = models.ForeignKey(DadosGestante, on_delete=models.CASCADE)
    semana_gestacao = models.IntegerField()
    altura_uterina = models.FloatField()


class Exames(models.Model):
    gestante = models.ForeignKey(DadosGestante, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    data = models.DateField()
    resultado = models.CharField(max_length=255)


class TratamentoSifilis(models.Model):
    gestante = models.ForeignKey(DadosGestante, on_delete=models.CASCADE)
    data_1_dose = models.DateField()
    data_2_dose = models.DateField()
    data_3_dose = models.DateField()


class Malaria(models.Model):
    gestante = models.ForeignKey(DadosGestante, on_delete=models.CASCADE)
    data = models.DateField()
    resultado = models.CharField(max_length=255)


class SuplementacaoFerro(models.Model):
    gestante = models.ForeignKey(DadosGestante, on_delete=models.CASCADE)
    mes = models.IntegerField()
    sim_nao = models.BooleanField()


class SuplementacaoAcidoFolico(models.Model):
    gestante = models.ForeignKey(DadosGestante, on_delete=models.CASCADE)
    mes = models.IntegerField()
    sim_nao = models.BooleanField()


class Ultrassonografia(models.Model):
    gestante = models.ForeignKey(DadosGestante, on_delete=models.CASCADE)
    data = models.DateField()
    ig_dum = models.CharField(max_length=255)
    ig_usg = models.CharField(max_length=255)
    peso_fetal = models.FloatField()
    placenta = models.CharField(max_length=255)
    liquido = models.CharField(max_length=255)
    outros = models.CharField(max_length=255)


class VacinaTetanica(models.Model):
    gestante = models.ForeignKey(DadosGestante, on_delete=models.CASCADE)
    sem_info_imunizacao = models.BooleanField()
    imunizada_menos_5_anos = models.BooleanField()
    imunizada_mais_5_anos = models.BooleanField()
    dose_1_data = models.DateField()
    dose_2_data = models.DateField()
    dose_3_data = models.DateField()
    reforco_data = models.DateField()


class HepatiteB(models.Model):
    gestante = models.ForeignKey(DadosGestante, on_delete=models.CASCADE)
    imunizada = models.BooleanField()
    dose_1_data = models.DateField()
    dose_2_data = models.DateField()


class Influenza(models.Model):
    gestante = models.ForeignKey(DadosGestante, on_delete=models.CASCADE)
    data = models.DateField()


class DTPa(models.Model):
    gestante = models.ForeignKey(DadosGestante, on_delete=models.CASCADE)
    data = models.DateField()


class Gestacoes(models.Model):
    gestante = models.ForeignKey(DadosGestante, on_delete=models.CASCADE)
    numero_gestacoes = models.IntegerField(null=True, blank=True)
    ectopica = models.IntegerField(null=True, blank=True)
    abortos = models.IntegerField(null=True, blank=True)
    parto = models.IntegerField(null=True, blank=True)
    pre_eclampsia_eclampsia = models.BooleanField(null=True, blank=True)
    cesarea = models.IntegerField(null=True, blank=True)
    parto_vaginal = models.IntegerField(null=True, blank=True)
    nascidos_vivos = models.IntegerField(null=True, blank=True)
    nascidos_mortos = models.IntegerField(null=True, blank=True)


class Consulta(models.Model):
    gestante = models.ForeignKey(DadosGestante, on_delete=models.CASCADE)
    data = models.DateField()
    queixa = models.TextField()
    ig_dum_usg = models.CharField(max_length=255)
    peso_imc = models.CharField(max_length=255)
    edema = models.CharField(max_length=255)
    pressao_arterial = models.CharField(max_length=20)
    altura_uterina = models.CharField(max_length=20)
    apresentacao_fetal = models.CharField(max_length=255)
    bcf_mov_fetal = models.CharField(max_length=255)
    toque_indicado = models.BooleanField()
    exantema = models.BooleanField()
    observacao_diagnostico_conduta = models.TextField()
