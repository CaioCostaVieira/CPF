# Validador de CPF/CNPJ

Uma aplicação web simples para validar e formatar números de CPF e CNPJ brasileiros.

## Funcionalidades

- Validação de CPF (11 dígitos)
- Validação de CNPJ (14 dígitos)
- Formatação automática (xxx.xxx.xxx-xx para CPF e xx.xxx.xxx/xxxx-xx para CNPJ)
- Cópia automática para área de transferência
- Opção para apenas formatar sem validar os dígitos verificadores

## Como usar

1. Acesse a aplicação
2. Digite o número de CPF ou CNPJ (com ou sem formatação)
3. Selecione se deseja apenas formatar (sem validar) ou validar completamente
4. Clique em "Validar" para ver o resultado
5. O resultado formatado será automaticamente copiado para sua área de transferência

## Tecnologias utilizadas

- Python 3.11
- Flask (Framework web)
- Bootstrap 5 (Framework CSS)
- JavaScript para interações do lado do cliente

## Como executar localmente

1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/validador-cpf-cnpj.git
   cd validador-cpf-cnpj
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```
   python main.py
   ```

4. Acesse no navegador:
   ```
   http://localhost:5000
   ```

## Deploy

### Opção 1: Deploy no GitHub Pages (somente frontend)

Para deploy apenas do frontend com chamadas de API para um backend separado, você precisará:

1. Configurar um servidor backend separado que fornecerá as APIs
2. Ajustar as chamadas de API no frontend para apontar para seu servidor

### Opção 2: Deploy completo em servidores ou plataformas de aplicações

Para deploy completo da aplicação (backend + frontend):

1. Você pode usar plataformas como Heroku, Render, PythonAnywhere, etc
2. Configure as variáveis de ambiente necessárias na plataforma escolhida
3. Para a maioria das plataformas, os arquivos `Procfile` e `requirements.txt` já estão configurados corretamente

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).