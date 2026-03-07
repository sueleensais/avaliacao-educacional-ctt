# Avaliação Educacional – Análise de Itens com CTT (Classical Test Theory)

## Descrição
Projeto de iniciativa própria desenvolvido em Python, com o objetivo de aplicar técnicas da Classical Test Theory (Teoria Clássica dos Testes) para avaliar a qualidade de questões de uma avaliação educacional. A análise busca identificar questões fáceis ou difíceis, verificar sua capacidade de discriminar entre alunos de diferentes níveis de desempenho e propor interpretações automáticas para apoiar decisões pedagógicas. Utilizei uma base de dados fictícia contendo 10 alunos e 100 questões.

## Metodologia
1. **Obtenção e tratamento dos dados**: leitura de uma matriz de respostas simuladas (0 = erro, 1 = acerto).  
2. **Cálculo da dificuldade**: proporção média de acertos por questão.  
   - Valores próximos de 1.0 → questões fáceis.  
   - Valores próximos de 0.0 → questões difíceis.  
3. **Cálculo da discriminação**: diferença de desempenho entre grupos de alunos (27% melhores vs. 27% piores).  
   - Valores positivos → boa discriminação.  
   - Valores próximos de 0 → discriminação fraca.  
   - Valores negativos → item problemático.  
4. **Visualização**: gráfico de barras comparando dificuldade e discriminação.  
5. **Interpretação automática**: criação de uma coluna classificando cada questão como **Boa**, **Fraca** ou **Revisar**.

## Resultados
A análise gerou uma tabela final com três indicadores principais:
- **Dificuldade**: mostra se a questão é fácil ou difícil.  
- **Discriminação**: mostra se a questão diferencia bem os alunos.  
- **Interpretação**: classificação automática baseada nos valores de discriminação.  

Exemplo de saída:

| Questão | Dificuldade | Discriminação | Interpretação |
|---------|-------------|---------------|---------------|
| Q1      | 0.75        | 0.45          | Boa           |
| Q2      | 0.60        | 0.20          | Fraca         |
| Q3      | 0.40        | -0.10         | Revisar       |

## Interpretações
- Questões **Boas**: alta discriminação, contribuem para diferenciar alunos.  
- Questões **Fracas**: pouca discriminação, podem ser mantidas com cautela.  
- Questões **Revisar**: discriminação negativa, devem ser reformuladas ou descartadas.  