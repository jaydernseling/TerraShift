# TerraShift
**Climate-Adaptive Crop Rotation Decision-Support Tool for Kota Samarahan – Asajaya, Sarawak**

## Overview
TerraShift helps smallholders in coastal Sarawak select resilient crop rotations by combining NASA Earth observations with local soil profiles (coastal alluvial gley clay vs. lowland tropical peat) and farmer priority weights.

## NASA Data & Software Used
- **NASA SMAP L4 (`SPL4SMGP`)** accessed via NASA's `earthaccess` Python library and `xarray`
- **NASA POWER Agroclimatology API (`community=AG`)** for daily rainfall, air temperature, humidity, and solar irradiance
- **NASA GIBS (MODIS Terra True Color)** satellite tile layers rendered via `Folium`

## How to Run Locally
1. Install dependencies: `pip install -r requirements.txt`
2. Authenticate NASA Earthdata once: `python test_nasa.py`
3. Launch the dashboard: `streamlit run app.py`

## Super Intelligence (SI) Disclosure
AI tools were used to assist with Python syntax scaffolding and documentation formatting. All problem framing, Sarawak agronomic parameters, and system integration were designed and verified by the team.