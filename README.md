# 🫀 Software de Modelagem 3D Cardiovascular 

## 📌 Sobre o Projeto 

Sistema para seleção, parametrização clínica e representação tridimensional interativa de segmentos vasculares do sistema cardiovascular. 

A aplicação permite que pesquisadores e profissionais de saúde selecionem artérias a partir de uma biblioteca visual (como artérias coronárias, aorta abdominal e carótida) e configurem parâmetros biométricos e clínicos reais (como grau de obstrução/estenose, deformações e alterações hemodinâmicas). 

Devido à alta complexidade computacional envolvida nos cálculos das simulações, o sistema utiliza uma arquitetura cliente-servidor distribuída: 

- **Front-end (React):** Interface do usuário para navegação na biblioteca, formulário de entrada de dados clínicos e renderização 3D interativa. 

- **Back-end Intermediário (Python / FastAPI / PyVista):** Gerenciamento da biblioteca de malhas 3D, comunicação via API e pós-processamento dos modelos. 

- **Servidor Remoto de Cálculo:** Processamento e solução das equações matemáticas complexas.