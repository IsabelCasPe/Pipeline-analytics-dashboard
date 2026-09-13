# Pipeline Analytics Dashboard

Um painel **enxuto e claro** para acompanhar o funil comercial - *stages*, conversões e **cycle time** - com delicadeza visual e rigor analítico.   
> *“O dado conta a história; o desenho só abre caminho.”* 💙

[![USP](https://img.shields.io/badge/USP-Dissertação-0A3D91?logo=academia&logoColor=white)](https://teses.usp.br/teses/disponiveis/3/3151/tde-20102010-122044/en.php)
[![arXiv](https://img.shields.io/badge/arXiv-2504.01969-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.01969)
[![JAES](https://img.shields.io/badge/JAES-Published-0B6E4F?style=for-the-badge&logo=readthedocs&logoColor=white)](https://ritha.eu/journals/JAES/issues/93/articles/7)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#license)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB.svg)](#technologies-used) 
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)](#dashboard) 

---

[![Instagram](https://img.shields.io/badge/📸_Instagram-@isabel__maths-C0C0C0?logo=instagram&logoColor=black)](https://www.instagram.com/isabel_maths/)
[![YouTube](https://img.shields.io/badge/▶_YouTube-IsabelCasPe_Maths_∞-C0C0C0?logo=youtube&logoColor=black)](https://www.youtube.com/@isabelcastillo4230)

---

## Table of Contents
- [About](#about)
- [Features](#features)
- [Dashboard](#dashboard)
- [Data Schema](#data-schema)
- [Technologies Used](#technologies-used)
- [How to Use](#how-to-use)
- [Repository Structure](#repository-structure)
- [Methodology](#methodology)
- [Contributing](#contributing)
- [Privacy](#privacy)
- [License](#license)

## About
Este projeto apresenta um **dashboard analítico de pipeline comercial**, focado em **stages**, **taxas de conversão** e **cycle time**.  
Foi criado para **domar o aparente “caos” do funil** e evidenciar competências de análise, modelagem e visualização — com elegância.

- **Stages (exemplo):** Lead → Qualificado → Proposta → Fechado.  
- **Métricas-chave:** *Value*, Conversion Rate, Cycle Time (P50/P90).  
- **Objetivo:** oferecer decisões rápidas com transparência metodológica.

## Features
- **Visão por estágio:** entradas, volumes e *drop-offs*.  
- **Conversões por etapa e período:** taxa efetiva e tendência.  
- **Cycle time / SLA:** média e dispersão (P50/P90) entre etapas.  
- **Alertas suaves:** bandas móveis para outliers e quedas de conversão.  
- **Anotações contextuais:** campanhas/sazonais para leitura honesta do funil.

## Dashboard
- Acesse o painel: **[link para o dashboard](#)**  
- Screenshot: `screenshots/dashboard.png`

> Dica: se usar Power BI, inclua um gif curto em `docs/` para mostrar interações.

## Data Schema
CSV/SQL mínimo:
- `deal_id`, `stage_from`, `stage_to`, `entered_at`, `exited_at`, `owner`, `value`  
- `source`, `segment`, `region` *(opcionais para recortes)*

O repositório inclui `data/sample_pipeline.csv` para testes locais.

## Technologies Used
- **Power BI** - visualizações e publicação.  
- **Python** - pré-processamento e métricas (Pandas/NumPy/Plotly/Matplotlib).  
- *(Opcional)* **Streamlit** - demo web local.

## How to Use
### A) Power BI
1. Abra `dashboard/PipelineAnalytics.pbix`.  
2. Em **Transform Data**, aponte as fontes (ou use `data/sample_pipeline.csv`).  
3. Ajuste medidas (conversion rate/cycle time) se mudar nomes de colunas.  
4. Clique em **Refresh** e publique (se desejar).


## Methodology
- **Conversão por etapa:** saídas/entradas por janela.
- **Cycle time:** média e quantis (P50/P90) de `entered_at` → `exited_at`.
- **Bandas móveis:** controle de variação para alertas contextuais.
- **Reprodutibilidade:** funções em `src/` para cada métrica e gráfico.

## Contributing
🤝 Contribuições são bem-vindas. Prefira PRs pequenos, com:
- descrição do antes/depois,
- prints do painel,
- e nota sobre dados usados (sintéticos/anonimizados).

## Privacy
🔐 Use apenas dados sintéticos ou anonimizados. Se for conectar fontes reais, mantenha segredos via variáveis de ambiente (.env) e não commite credenciais.

## License
 Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) pra mais detalhes.Feito com ciência, carinho e um pouco de caos domado. ✨
@IsabelCasPe - 2025 • Portfólio: github.com/IsabelCasPe


# Pipeline Analytics Dashboard
Um dashboard interativo feito com Streamlit pra mostrar performance e domar o caos! 😎 @caradocaos, tenta bagunçar isso aqui!

## Como rodar
1. Clone o repo: `git clone https://github.com/IsabelCasPe/Pipeline-analytics-dashboard`
2. Instale as dependências: `pip install -r requirements.txt`
3. Rode o app: `streamlit run dashboard.py`
4. Abra no navegador e clique em "Domar o Caos"! ✨

Feito com ciência, carinho e #CaosDomado! 💎

## Sobre
Desenvolvido por Ana Isabel Castillo Pereda. Veja mais em [isabelcaspe.github.io](https://isabelcaspe.github.io).

### B) Python / Streamlit
```bash
# Requisitos: Python 3.10+
pip install -r requirements.txt
streamlit run app.py
