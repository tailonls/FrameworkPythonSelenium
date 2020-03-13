# FrameworkPythonSelenium

## Instalações: 

	No CMD:
	
	- Instalar Python (Lembrar de marcar para configurar as path variables)
	- pip install selenium (Biblioteca do Selenium)
	- pip install behave (Biblioteca do BDD)
	- pip install webdriver_manager (vai trabalhar com a versão mais atual do driver)
	- Instalar Pycharm
	
## Configurar Pycharm:
	
	- Menu File -> Settings -> Project -> Project Interpreter -> Selecione a versão do Python instalada e confirme.

## Instalar driver:

	- Baixar drivers:
	
		Chorome: https://sites.google.com/a/chromium.org/chromedriver/downloads
		Edge e IE: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

	- Cole os drivers na pasta Python\Python37-32\Scripts onde o python foi instalado. 

## Configurar variaveis de ambiente:

	- Este Computador -> Propiedades -> Configurações avançadas do sistema -> Variavéis de ambiente
	- Em Path adicione duas novas variaveis:
	
		caminho_ate_aqui/Python/Python37-32/
		caminho_ate_aqui/Python/Python37-32/Scripts

================================================================================

## Virtualenv:

	Utilizando gerenciadores (como pyenv, virtualenv, venv, pipenv) para criar ambientes e instalar nesses ambientes os pacotes ao inves de instalar na máquina.
	
	pip install pipenv (instalar pipenv)
	pipenv install selenium (vai criar um virtualenv com o nome do projeto)
	pipenv shell (para ativar o virtualenv criado)

## Para rodar teste:

	Para executar uma feature especifica: 
		behave features/nome_da_feature.feature
	
	Para executar uma tag especifica: 
		behave --tags=nome_da_tag
		ou behave -t nome_da_tag
		
	Para executar todas as tags com exceção de uma tag especifica, coloca o simbolo de menos na frente da tag:
		behave --tags=-nome_da_tag
		
	Para executar duas no mesmo comando:
		behave -t=nome_da_tag -t=nome_da_tag

