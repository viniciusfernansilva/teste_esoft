# teste_esoft
Teste Prático - Projeto em django
## Requerimentos de instalação
```bash
pip install -r requirements.txt
```
## Requerimentos para execução
* Criar base de dados conforme o arquivo `settings.py` (Utilizar wampserver ou derivados, por exemplo);
* Modificar usuário, senha e localização conforme desejar;
* Executar os seguintes comandos na ordem:
```bash
python manage.py migrate
```
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```
