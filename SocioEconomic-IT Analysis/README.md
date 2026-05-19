<h1 align="center">Socio-Economic Factors for IT Growth in India - Analysis</h1>

<p align="center">
  <img src="projectimage.png" width="900">
</p>

## Project Overview

India’s Information Technology sector has expanded rapidly over the past few decades and has become one of the major contributors to economic growth. However, IT development is not evenly distributed across all states. Some regions emerged as strong technology hubs while others lagged behind.

This project investigates whether long-term socio-economic indicators such as literacy rate, population size, and urbanization can help explain future IT growth patterns across Indian states.

Rather than studying IT growth in isolation, this analysis attempts to understand whether underlying social and demographic conditions influence the development of technology ecosystems.

---

## Objective

To analyze relationships between socio-economic indicators and state-wise IT growth in India and identify which factors appear most associated with future IT expansion.

---

## Problem Statement

The project attempts to answer the following questions:

- Does larger population size contribute to stronger IT growth?
- Is literacy associated with future IT expansion?
- Does urbanization create favorable conditions for technology development?
- Which socio-economic factor appears most influential?

---

## Dataset Information

The project combines multiple publicly available datasets:

| Dataset | Description |
|----------|-------------|
| IT Export Data | State-wise IT export values |
| Literacy Data | Literacy percentages across states |
| Population Data | State population statistics |
| Urban Population Data | Urbanization indicators |

### Data Sources

- data.gov.in
- Reserve Bank of India (RBI)
- Public demographic datasets

---

## Data Preprocessing

Data preparation involved multiple cleaning and transformation steps:

- Standardized state names across datasets
- Removed inconsistent entries
- Removed most Union Territories
- Combined Andhra Pradesh and Telangana values where required
- Merged datasets using SQL operations
- Performed consistency checks before analysis

---

## Exploratory Analysis

The following analyses were performed:

- Population vs IT Growth
- Literacy vs IT Growth
- Urban Population vs IT Growth
- Correlation analysis
- Comparative trend analysis

---

## Visualizations

The project includes:

- Scatter plots
- Correlation heatmaps
- Bar charts
- Trend comparisons
- Relationship analysis graphs

---

## Key Findings

- States with larger urban populations generally show stronger IT growth patterns.
- Literacy demonstrates a positive relationship with technology expansion.
- Population alone is not a reliable predictor of IT success.
- Multiple socio-economic indicators together provide stronger insights than individual factors.

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- SQLite
- Jupyter Notebook

---

## Project Structure

```text
SocioEconomic-IT-Analysis/
│
├── Socio economic factors for IT Growth in India.ipynb
├── literacy.csv
├── urban population.xlsx
├── state population.xlsx
├── it export.csv
├── projectimage.png
└── README.md
```

---

## Conclusion

The analysis suggests that socio-economic conditions may influence long-term technology growth. Population size alone does not explain why certain regions become technology hubs. Educational development and urban infrastructure appear to play a stronger role in creating environments that support IT expansion.

Future work could include additional variables such as GDP, employment statistics, internet penetration, and government investment indicators.

---

## Author

**Jyothis P K**

GitHub: https://github.com/JYOTHISPK
