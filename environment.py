from browser import Browser
from utils.reporte_util import Reporte_util

report = Reporte_util()


# executa os comandos antes de todos os testes iniciarem
def before_all(context):
    context.browser = Browser()


# executa os comandos depois de todos os testes terminarem
def after_all(context):
    context.browser.browser_quit()


# executa os comandos antes de cada cenario
def before_scenario(context, scenario):
    report.inicializa_report()
    report.add_test_in_report(scenario, 1)
    print(scenario)


# executa os comandos entre cada cenario
def after_scenario(context, scenario):
    context.browser.browser_clear()
    report.finaliza_report()
