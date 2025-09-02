# -----------------------
# Import necessary libraries
# -----------------------
import hashlib  # For hashing blocks using SHA-256
import json     # For serializing data to JSON
from time import time  # For timestamps (not used, but can measure block time)
from datetime import datetime  # For human-readable timestamps
import pandas as pd  # For handling tabular data in the dashboard
from flask import Flask, request, jsonify  # Flask web framework (not used currently)
import streamlit as st  # For creating a dashboard interface
import threading  # To run Streamlit in a separate thread if needed

# -----------------------
# Define a Block in the blockchain
# -----------------------
class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index  # Block's position in the chain
        self.timestamp = timestamp  # When the block was created
        self.data = data  # Actual data stored in the block
        self.previous_hash = previous_hash  # Hash of the previous block
        self.nonce = nonce  # Nonce for Proof-of-Work
        self.hash = self.compute_hash()  # Compute the block's hash on creation

    # Compute SHA-256 hash of the block contents
    def compute_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()  # Encode the dictionary as JSON string
        return hashlib.sha256(block_string).hexdigest()  # Return SHA-256 hash

# -----------------------
# Define the Blockchain
# -----------------------
class Blockchain:
    difficulty = 2  # PoW difficulty: number of leading zeros required

    def __init__(self):
        self.chain = []  # List to store blocks
        self.create_genesis_block()  # Initialize blockchain with the first block

    # Create the genesis block (first block in the chain)
    def create_genesis_block(self):
        genesis_block = Block(0, str(datetime.now()), "Genesis Block", "0")
        self.chain.append(genesis_block)

    # Property to easily get the last block
    @property
    def last_block(self):
        return self.chain[-1]

    # Proof-of-Work algorithm
    def proof_of_work(self, block):
        block.nonce = 0  # Reset nonce
        computed_hash = block.compute_hash()  # Initial hash
        # Keep iterating until hash starts with 'difficulty' zeros
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash  # Return valid hash

    # Add a new block with the given data
    def add_block(self, data):
        new_block = Block(
            index=self.last_block.index + 1,
            timestamp=str(datetime.now()),
            data=data,
            previous_hash=self.last_block.hash
        )
        new_block.hash = self.proof_of_work(new_block)  # Find valid hash
        self.chain.append(new_block)  # Add to blockchain
        return new_block

# -----------------------
# Define Blue Carbon Token System
# -----------------------
class BlueCarbonToken:
    def __init__(self, name="BlueCarbonToken", symbol="BCT"):
        self.name = name
        self.symbol = symbol
        self.balances = {}  # Dictionary to hold user token balances
        self.total_supply = 0  # Total tokens issued

    # Issue tokens to a user
    def issue(self, user, amount):
        self.balances[user] = self.balances.get(user, 0) + amount
        self.total_supply += amount  # Update total supply

    # Transfer tokens between users
    def transfer(self, sender, receiver, amount):
        if self.balances.get(sender, 0) >= amount:
            self.balances[sender] -= amount
            self.balances[receiver] = self.balances.get(receiver, 0) + amount
            return True
        return False

# -----------------------
# Sample users
# -----------------------
users = {
    "NCCR_Admin": "admin@example.com",
    "NGO_1": "ngo1@example.com",
    "Community_1": "community1@example.com"
}

# -----------------------
# Initialize blockchain and token system
# -----------------------
token_system = BlueCarbonToken()
carbon_chain = Blockchain()

# -----------------------
# Sample carbon project data
# -----------------------
sample_data = [
    {"project_name":"Mangrove Restoration", "location":"Goa", "area_ha":5, "species":"Rhizophora", "CO2_absorbed_tonnes":50, "submitted_by":"NGO_1"},
    {"project_name":"Seagrass Planting", "location":"Kerala", "area_ha":3, "species":"Halodule", "CO2_absorbed_tonnes":30, "submitted_by":"Community_1"}
]

# -----------------------
# Add projects to blockchain and issue tokens
# -----------------------
for entry in sample_data:
    block = carbon_chain.add_block(entry)  # Add project as a block
    token_system.issue(entry['submitted_by'], entry['CO2_absorbed_tonnes'])  # Issue tokens
    print(f"Added block {block.index} with hash {block.hash} and issued {entry['CO2_absorbed_tonnes']} BCT to {entry['submitted_by']}")

# -----------------------
# Functions to display blockchain and token balances
# -----------------------
def view_chain():
    for block in carbon_chain.chain:
        print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}, Prev: {block.previous_hash}")

def view_balances():
    print("=== Token Balances ===")
    for user, balance in token_system.balances.items():
        print(f"{user}: {balance} BCT")

# Display blockchain and balances
view_chain()
view_balances()

# -----------------------
# Streamlit Dashboard
# -----------------------
def run_dashboard():
    st.title("Blue Carbon Registry Dashboard")
    st.subheader("Registered Projects")

    # Skip genesis block for display
    projects = [block.data for block in carbon_chain.chain[1:]]
    df = pd.DataFrame(projects)
    st.dataframe(df)

    st.subheader("Token Balances")
    balances_df = pd.DataFrame(list(token_system.balances.items()), columns=["User", "BCT Balance"])
    st.dataframe(balances_df)

# -----------------------
# Save Streamlit dashboard to file
# -----------------------
with open("dashboard.py", "w") as f:
    f.write("""
import streamlit as st
import pandas as pd

# Sample blockchain data
projects = [
    {"project_name":"Mangrove Restoration", "location":"Goa", "area_ha":5, "species":"Rhizophora", "CO2_absorbed_tonnes":50, "submitted_by":"NGO_1"},
    {"project_name":"Seagrass Planting", "location":"Kerala", "area_ha":3, "species":"Halodule", "CO2_absorbed_tonnes":30, "submitted_by":"Community_1"},
    {"project_name":"Coral Reef Restoration", "location":"Andaman", "area_ha":2, "species":"Acropora", "CO2_absorbed_tonnes":20, "submitted_by":"NGO_1"}
]

# Sample token balances
balances = {
    "NGO_1": 70,
    "Community_1": 30,
    "NCCR_Admin": 0
}

st.title("Blue Carbon Registry Dashboard")
st.subheader("Registered Projects")
df = pd.DataFrame(projects)
st.dataframe(df)

st.subheader("Token Balances")
balances_df = pd.DataFrame(list(balances.items()), columns=["User", "BCT Balance"])
st.dataframe(balances_df)
""")

# -----------------------
# Ngrok setup for Colab / remote access
# -----------------------
from pyngrok import ngrok

# Set your Ngrok token here
!ngrok authtoken "Enter your token from NGROK PLATFORM"

# Run Streamlit in background
get_ipython().system_raw("streamlit run dashboard.py &")

# Open Ngrok tunnel on default Streamlit port
public_url = ngrok.connect(8501)
print("🚀 Open this URL to access the dashboard:")
print(public_url)
