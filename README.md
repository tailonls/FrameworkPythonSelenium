# FrameworkPythonSelenium

### Framework utiliza:
- Linguagem Python
- Selenium
- Behave (BDD)

### Instalações:

- Instalar Python (Lembrar de marcar para configurar as path variables)
- pip install selenium
- pip install behave
- pip install nose
- Instalar Pycharm	

### Configurar Variaveis de ambiente Python:

Este Computador -> Propiedades -> Configurações avançadas do sistema -> Variavéis de ambiente
Em Path adicione duas novas variaveis:

PY_HOME:

    C:\Users\seu_nome\AppData\Local\Programs\Python\Python37-32

PATH:	

    %PY_HOME%/Python/Python37-32/
    %PY_HOME%/Python/Python37-32/Scripts

### Adicionar Chromedriver nas Variaveis de ambiente:

    Colocar o driver na pasta: C:\bin
    Nas variaveis do sistemas -> PATH: C:\bin (depois do ;) 
    Testar com: chromedriver.exe -v

**OU:**

    Cole os drivers na pasta Python\Python37-32\Scripts onde o python foi instalado.


### Configurar Pycharm:

Menu File -> Settings -> Project -> Project Interpreter -> Selecione a versão do Python instalada e confirme.

### Instalar driver:

Baixar drivers:

- Chorome: https://sites.google.com/a/chromium.org/chromedriver/downloads

- Edge e IE: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

- Cole os drivers na pasta Python\Python37-32\Scripts onde o python foi instalado. 

### Para rodar teste:

Para executar uma feature especifica: 
	
	behave
	behave features\nome_da_feature.feature
	
Para executar uma tag especifica: 

	behave --tags=nome_da_tag
	ou behave -t nome_da_tag
		
Para executar todas as tags com exceção de uma tag especifica, coloca o simbolo de menos na frente da tag:

	behave --tags=-nome_da_tag
		
Para executar duas no mesmo comando:

	behave -t=nome_da_tag -t=nome_da_tag

### Comandos PIP (Python Install Package):

    pip install nome_pacote==2.53 (versão específica)
    pip install nome_pacote~=2.53 (ultima versão compativel ex.: 2.53.6)
    pip install -U nome_pacote (ultima versão)
    
    pip uninstall nome_pacote

    pip list (lista pacotes instalados)	
    pip list --outdated, -o (lista versao mais recente dos pacotes instalados)	

    pip show nome_pacote(mostra dados do pacote instalado)
    pip show -f nome_pacote(mostra arquivos do pacote instalado)
    
    pip search nome_pacote (Procura um pacote/projeto que contém aquele nome)

    pip download nome_pacote -d C:/Users/pasta_qualquer (Baixa pacote para pasta, obs.: abrir cmd como adm!)
    pip install C:/Users/pasta_qualquer/nome_pacote_baixado.whl (Instala pacote do arquivo já baixado)

    pip install -r requirements.txt (Instala pacotes listados no arquivo requirements.txt)
    pip uninstall -r requirements.txt (desinstala pacotes listados no arquivo requirements.txt)	
    pip freeze > requirements.txt (Cria lista/lista pacotes no arquivo requirements.txt)
