# 🤖 Automação de Cadastro de Produtos (RPA com Python)

Este projeto automatiza o cadastro de produtos em um sistema web utilizando Python, simulando ações humanas como clique, digitação e navegação.

## 🚀 Objetivo

Reduzir o tempo gasto em tarefas repetitivas de cadastro manual de produtos em sistemas empresariais.

## 🛠️ Tecnologias utilizadas

- Python
- PyAutoGUI
- Pandas

## 📂 Como funciona

1. Abre o sistema
2. Realiza login automático
3. Lê uma base de produtos (CSV)
4. Preenche automaticamente os campos do sistema
5. Repete até finalizar todos os produtos

## 📊 Estrutura do CSV

O arquivo deve conter:

- código
- marca
- tipo
- categoria
- preco_unitario
- custo
- obs

## ▶️ Como executar

```bash id="m1x9qp"
pip install -r requirements.txt
python main.py
```

⚠️ Observações
O script depende da posição da tela (coordenadas do PyAutoGUI)
Recomendado ajustar pyautogui.position() antes de rodar.


👨‍💻 Autor

Projeto desenvolvido por Ercilio Zamar
Estudante de Análise e Desenvolvimento de Sistemas com foco em automação e Python.
