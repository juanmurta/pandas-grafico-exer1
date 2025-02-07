# Análise de Vendas com Python e Visualização de Dados  

## Descrição  
Este script realiza a importação, limpeza e análise de dados de vendas de uma empresa. Ele combina informações de diferentes arquivos CSV, filtra lojas específicas e gera visualizações gráficas utilizando `matplotlib` e `seaborn`.  

## Como Usar  

1. **Pré-requisitos**  
   - Ter os arquivos CSV armazenados no caminho especificado no código.  
   - Instalar as bibliotecas necessárias executando:  

     ```bash
     pip install pandas matplotlib seaborn
     ```  

2. **Estrutura dos Arquivos CSV**  
   O script espera os seguintes arquivos:  

   - `Contoso - Vendas - 2017.csv`: Contém informações das vendas realizadas, incluindo ID do cliente, ID do produto, ID da loja e quantidade vendida.  
   - `Contoso - Cadastro Produtos.csv`: Contém a relação de produtos vendidos e seus respectivos IDs.  
   - `Contoso - Lojas.csv`: Contém a relação de lojas e seus respectivos IDs.  
   - `Contoso - Clientes.csv`: Contém os dados dos clientes, incluindo e-mails.  

3. **Execução do Script**  
   - Certifique-se de que os arquivos CSV estejam no caminho correto (`E:\Cursos\Estudos\Impressionador\PowerBi`).  
   - Execute o script no terminal ou em um ambiente Python:  

     ```bash
     python nome_do_arquivo.py
     ```  

4. **O que o Script Faz**  
   - Importa e mescla os dados de diferentes fontes.  
   - Filtra os dados para incluir apenas as lojas com IDs 86, 306 e 172.  
   - Converte a coluna "Data da Venda" para o formato de data.  
   - Gera gráficos de vendas ao longo do tempo usando `matplotlib` e `seaborn`.  

## Contribuindo para o projeto  
1. Para contribuir com este projeto, siga estas etapas:  
2. Bifurque este repositório.  
3. Crie um branch: `git checkout -b <nome_branch>`.  
4. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`.  
5. Envie para o branch original: `git push origin <nome_do_projeto>/<local>`.  
6. Crie a solicitação de pull.  

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).  
