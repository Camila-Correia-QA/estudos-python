fake = Fake Br
 telefone_aleatorio = input.fake.cellphone
    with allure.step("validar telefone"):
        validar_telefone = page.locator("#x")
        expect(validar_telefone).to_have_(telefone_aleatorio)
