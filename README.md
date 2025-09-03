# Pipeline Analytics Dashboard

Um painel **enxuto e claro** para acompanhar o funil comercial — *stages*, conversões e **cycle time** — com delicadeza visual e rigor analítico.  
> *“O dado conta a história; o desenho só abre caminho.”*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#license)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB.svg)](#technologies-used)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)](#dashboard)

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
- **Power BI** — visualizações e publicação.  
- **Python** — pré-processamento e métricas (Pandas/NumPy/Plotly/Matplotlib).  
- *(Opcional)* **Streamlit** — demo web local.

## How to Use
### A) Power BI
1. Abra `dashboard/PipelineAnalytics.pbix`.  
2. Em **Transform Data**, aponte as fontes (ou use `data/sample_pipeline.csv`).  
3. Ajuste medidas (conversion rate/cycle time) se mudar nomes de colunas.  
4. Clique em **Refresh** e publique (se desejar).

---
### 🤝 Contribuições

Pull requests são bem-vindos. Prefira PRs pequenos, com descrição do antes/depois e evidências visuais (print do painel).
---

### 🔐 Privacidade

Use apenas dados sintéticos ou anonimizados. Se for conectar fontes reais, mantenha segredos via variáveis de ambiente (.env) e não commite credenciais.
---
###📜 Licença

MIT — ver LICENSE. Use, melhore e compartilhe com crédito.

Feito com ciência, carinho e um pouco de caos domado.
@IsabelCasPe – 2025 • Portfólio: github.com/IsabelCasPe

### B) Python / Streamlit
```bash
# Requisitos: Python 3.10+
pip install -r requirements.txt
streamlit run app.py
