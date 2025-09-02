# Blue Carbon Blockchain & Token Registry

A Python-based blockchain application for tracking carbon offset projects and issuing **Blue Carbon Tokens (BCT)** as rewards for verified carbon sequestration activities. Includes a **Streamlit dashboard** for visualizing projects and token balances and can be accessed remotely via **ngrok**.  

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Installation](#installation)  

---

## Overview

The **Blue Carbon Registry** project allows environmental organizations, communities, and administrators to:

- Record carbon offset projects (e.g., mangrove restoration, seagrass planting).  
- Store project data securely on a blockchain.  
- Reward contributors with **Blue Carbon Tokens (BCT)** based on CO₂ absorbed.  
- Visualize registered projects and token balances through a modern dashboard.

This system ensures **data integrity**, **transparency**, and **tokenized incentives** for carbon sequestration projects.  

---

## Features

- **Blockchain Implementation**  
  - Custom `Block` and `Blockchain` classes.  
  - Proof-of-Work algorithm for block validation.  
  - Automatic hash computation and nonce handling.  

- **Blue Carbon Token (BCT) System**  
  - Issue tokens to project contributors based on CO₂ absorption.  
  - Transfer tokens between users.  
  - Track total token supply and balances.  

- **Dashboard**  
  - Streamlit-based web dashboard.  
  - Displays registered projects and token balances.  
  - Accessible remotely via ngrok.  

- **Sample Data**  
  - Includes example projects for Mangrove Restoration, Seagrass Planting, and Coral Reef Restoration.  

---

## Tech Stack

- **Programming Language:** Python 3.10+  
- **Blockchain & Hashing:** `hashlib`, `json`  
- **Data Handling:** `pandas`  
- **Dashboard:** `streamlit`  
- **Remote Access:** `ngrok`  
- **Web Framework (optional):** `flask`  

---

## Installation

1. **Clone the repository**  
```bash
git clone https://github.com/Dhanesh10war/Blockchain/Blue_Carbon_Credit.git
cd Blue_Carbon_Credit
