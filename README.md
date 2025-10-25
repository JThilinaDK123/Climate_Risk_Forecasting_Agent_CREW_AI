# Climate Risk Forecasting Agents (CrewAI Framework)

## Overview
This project uses a **multi-agent system** built on the **CrewAI framework** to perform **climate risk forecasting and reporting** for any given location and date.  
The agents collaborate to research, analyze, and report emerging environmental risks such as **droughts**, **floods**, and **wildfires**, leveraging satellite-derived indices (NDVI, NDMI, NDRI) and atmospheric data with the helop of surper tool.

The framework integrates advanced geospatial data analysis with natural language summarization, enabling automated research synthesis and climate intelligence reporting.

---

## System Architecture

The system is composed of **two specialized AI agents**:

### 1. `climate_researcher`
**Role:** Climate Risk Senior Data Researcher  
**Model:** `openai/gpt-4o-mini`  

**Goal:**  
Investigate emerging scientific and technological advancements in **climate risk forecasting** for a specified `{location}` and `{date}`.  
The agent focuses on environmental indicators such as:
- NDVI (Normalized Difference Vegetation Index)
- NDMI (Normalized Difference Moisture Index)
- NDRI (Normalized Difference Redness Index)
- Soil moisture and atmospheric variables  

**Backstory:**  
A veteran environmental scientist skilled in geospatial analytics, satellite observation, and climate modeling.  
The researcher continuously reviews datasets like **MODIS**, **Sentinel**, and **Landsat** to identify anomalies, trends, and modeling innovations relevant to climate risk forecasting.

**Task: `research_task`**
- **Description:**  
  Conducts an advanced investigation into climate risk forecasting for `{location}`.  
  Analyzes the latest scientific literature, Earth observation datasets, and predictive modeling techniques.  
- **Expected Output:**  
  A Markdown file (`output/research_findings.md`) containing **10 bullet points** summarizing the most significant findings, datasets, and modeling approaches as of `{date}`.

---

### 2. `climate_reporting_agent`
**Role:** Climate Risk Reporting Analyst  
**Model:** `openai/gpt-4o-mini`  

**Goal:**  
Transform technical climate research outputs into **clear, actionable reports** for decision-makers and policymakers.  
This includes summarizing geospatial and atmospheric trends, forecasting outcomes, and highlighting key environmental risk drivers.

**Backstory:**  
An expert communicator skilled in turning complex model outputs into accessible insights.  
They prepare detailed summaries emphasizing implications such as:
- Increasing wildfire probability  
- Flood vulnerability  
- Vegetation health decline  
- Soil moisture depletion  

**Task: `reporting_task`**
- **Description:**  
  Synthesizes all research and analytical outputs into a comprehensive Markdown report.  
  Explains how geospatial indicators and weather trends contribute to forecasted risks for `{location}` at `{date}`.  
- **Expected Output:**  
  A well-structured climate risk report (`output/final_climate_risk_report.md`) including:
  - Executive Summary  
  - Methodology Overview  
  - Risk Interpretation  
  - Policy Recommendations  

**Context:**  
Uses results from `research_task` as input.

---


## How It Works

1. **Research Phase**  
   The `climate_researcher` agent investigates recent climate forecasting advancements, compiling structured findings into `output/research_findings.md`.

2. **Reporting Phase**  
   The `climate_reporting_agent` reviews the researcher’s findings, interprets key trends (e.g., NDVI decline, NDMI anomalies), and generates a full report in `output/final_climate_risk_report.md`.

3. **Output Example**
   - Detailed environmental indicator trends  
   - Risk factor correlations  
   - Region-specific hazard projections  
   - Policy-relevant insights  

---

## Variables

| Variable | Description |
|-----------|--------------|
| `{location}` | Target location or region for climate risk forecasting |
| `{date}` | Time period or projection date for analysis |
| `{current_year}` | Current operational year for context in research and modeling |

---

## Data Sources

The agents utilize or reference:
- **MODIS (Moderate Resolution Imaging Spectroradiometer)**
- **Sentinel (ESA Copernicus Mission)**
- **Landsat (USGS & NASA)**
- **Regional Climate Models (RCMs)**
- **Peer-reviewed climate forecasting studies**
- **Geospatial and meteorological datasets**

---

## Example Use Case

Forecasting wildfire and drought risks for **California, USA** for **2026**:

```yaml
location: California
date: 2026
current_year: 2025


