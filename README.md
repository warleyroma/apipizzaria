# 🍕 API para Sistema de Pizzaria  

Este repositório contém a implementação de uma **API REST robusta e escalável** para gerenciar pedidos de uma pizzaria. A API permite o cadastro de clientes, produtos, pedidos e o acompanhamento do status das entregas, garantindo uma experiência fluida para os usuários.  

## 🚀 Funcionalidades  
- ✅ Gerenciamento de clientes (cadastro, listagem, atualização e remoção)  
- ✅ Gerenciamento de produtos do cardápio (pizzas, bebidas e acompanhamentos)  
- ✅ Criação e acompanhamento de pedidos com status dinâmico  
- ✅ Integração com banco de dados **MySQL** hospedado em uma instância **AWS EC2**
- ✅ Gerenciamento eficiente do banco de dados com **MySQL Workbench**, permitindo consultas, modelagem e administração da instância MySQL na AWS EC2.
- ✅ Deploy da API na **Render**, tornando-a acessível globalmente  
- ✅ **Testes e documentação via Postman**, garantindo um fluxo de requisições eficiente e validado

## ⚙️ Infraestrutura e Ferramentas Utilizadas

- **MySQL Workbench**: Utilizado para gerenciar, modelar e consultar o banco de dados **MySQL** hospedado na AWS EC2.
- **AWS EC2**: Instância na nuvem que hospeda o banco de dados **MySQL**, proporcionando escalabilidade e alto desempenho.
- **Render**: Plataforma de deploy utilizada para disponibilizar a API de forma rápida e escalável.
- **Postman**: Ferramenta essencial para testes e documentação da API, permitindo a validação de requisições e resposta de dados de forma eficiente.

## 🛠️ Tecnologias Utilizadas  
- **FastAPI** para criação da API  
- **MySQL** como banco de dados  
- **MySQL Connector** para comunicação com o banco  
- **Uvicorn** para execução do servidor  
- **Render** para deploy da API  
- **Postman** para validação e testes avançados das requisições  

## ⚙️ Como Executar  

### 1️⃣ Clone o repositório  
```bash
git clone https://github.com/seu-usuario/api-pizzaria.git
cd api-pizzaria
