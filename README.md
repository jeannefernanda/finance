# finance
Projeto desenvolvido durante o evento PYSTACK WEEK 7.0

## Como rodar o projeto?

* Clone esse repositório
* Crie um virtualenv
* Ative o virtualenv
* Instale as dependências
* Rode as migrações

```bash
git clone https://github.com/jeannefernanda/finance.git
cd finance
python -m venv .venv
.venv/Scripts/Activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
## ATENÇÃO!
No windows é necessário instalar o <a href="https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows">GTK<a> para utilizar a biblioteca weasyprint para gerar pdf.
