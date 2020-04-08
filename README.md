# FrameworkPythonSelenium

### Framework utiliza:
- Linguagem Python
- Selenium
- Behave (BDD)

### Requisitos para rodar o teste:
- behave
- selenium
- nose
- Chrome Driver no path do sistema

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

### Configurar Variaveis de ambiente Python:

- Variaveis do sistemas:
    - PY_HOME: C:\Users\seu_nome\AppData\Local\Programs\Python\Python37-32

- PATH:
    - %PY_HOME%\Scripts
    - %PY_HOME%
        
### Adicionar Chromedriver nas Variaveis de ambiente:
    
- Colocar o driver na pasta: __C:\bin__
- Nas variaveis do sistemas -> PATH: __C:\bin__ (depois do ;) 
- Testar com: __chromedriver.exe -v__
