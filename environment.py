from browser import Browser


# executa os comandos antes de todos os testes iniciarem
def before_all(context):
    context.browser = Browser()


# executa os comandos depois de todos os testes terminarem
def after_all(context):
    context.browser.browser_quit()


# executa os comandos entre cada cenario
def after_scenario(context, scenario):
    context.browser.browser_clear()
