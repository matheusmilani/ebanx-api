
# Inicialização do sistema
Para inicializar o sistema, é necessário:
- Python 3.7 ou superior
- Banco SQL ou similar (caso queira usar sqlite3, apenas não altere o environment)

## Instalação
Como recomendação, sugiro a criação de uma virtual env para não sujar o SO e a pasta de instalação padrão do Python.

Para instalar as dependências, use:
> pip install -r requirements.txt

Lembre-se de atualizar o environment com as credenciais de sua preferência


## Run
Para rodar o sistema, use:
> flask run

ou caso queira:
> python app.py

Após rodar o sistema, faça uma requisição para qualquer URL, isso consolida a database.
Ressalto que para o primeiro caso, as tabelas serão criadas automaticamente junto com as seeds de banco para inicializar o projeto.


# Tests
Foram feitos no total de 62 testes unitários e de integração para validar as ações do sistema, com cobertura de 87%.

Para rodar os testes, use:
> pytest tests\\models tests\\resources tests\\helpers --disable-pytest-warnings -v
