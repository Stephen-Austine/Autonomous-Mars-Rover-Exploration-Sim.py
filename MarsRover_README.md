# 🚀 Autonomous Mars Rover Exploration Simulation

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/AI-Agent--Based-FF6B35?style=for-the-badge)
![Simulation](https://img.shields.io/badge/Type-Simulation-9B59B6?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A Python-based intelligent agent simulation modelling an autonomous Mars rover exploring a dynamic environment, detecting rock samples, and making decisions across multiple exploration rounds. Built around core AI agent principles: **perception**, **decision-making**, and **action**.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Classes & Architecture](#-classes--architecture)
- [Sample Output](#-sample-output)
- [Getting Started](#-getting-started)
- [Concepts Demonstrated](#-concepts-demonstrated)
- [Possible Extensions](#-possible-extensions)

---

## 🌍 Overview

This simulation models a Mars rover agent operating in an environment with four locations. Each location may or may not contain rock samples — determined randomly. The rover autonomously explores, samples rocks where available, avoids re-sampling already-visited locations, and adapts when the environment changes between exploration rounds.

The project is a practical demonstration of a **simple reflex agent** with state memory, operating in a **partially observable, dynamic environment**.

---

## ⚙️ How It Works

1. The Mars environment is initialised with 4 locations, each randomly assigned a condition (rocks present or absent).
2. The rover performs its **first exploration** — visiting each location, sampling rocks where found, and tracking visited sites.
3. The environment **changes dynamically** (rock conditions are re-randomised), simulating Mars surface activity.
4. The rover performs a **second exploration** — skipping already-sampled locations, and collecting new samples from newly available ones.
5. A **performance summary** is printed showing total samples collected and locations visited.

---

## 📁 Project Structure

```
Autonomous-Mars-Rover-Exploration-Sim/
│
└── Autonomous-Mars-Rover-Exploration-Sim.py    # Main simulation script
```

---

## 🏗️ Classes & Architecture

### `MarsEnvironment`
Represents the simulated Mars surface.

| Method | Description |
|---|---|
| `__init__()` | Initialises 4 named locations with randomly assigned rock conditions (0 = no rocks, 1 = rocks) |
| `change_environment()` | Re-randomises all location conditions to simulate environmental change |
| `display_environment()` | Prints the current rock status of each location |

### `RoverAgent`
The autonomous agent — perceives its environment and acts accordingly.

| Attribute / Method | Description |
|---|---|
| `sampled_locations` | A `set` tracking already-visited locations (prevents re-sampling) |
| `samples_collected` | Counter for total rock samples gathered |
| `explore()` | Iterates over all locations — samples rocks if present and not yet visited, skips otherwise |
| `display_performance()` | Prints a summary of the rover's results |

### `RoverPerformance`
The simulation controller — wires up the environment and agent, and runs the full two-round simulation.

| Method | Description |
|---|---|
| `run_simulation()` | Displays environment state, runs exploration round 1, changes environment, runs round 2, prints summary |

---

## 🖥️ Sample Output

```
Mars Environment (Before 1st exploration):
Location A: Rocks available
Location B: No rocks
Location C: Rocks available
Location D: No rocks

Rover starting exploration venture...
Sampling rocks at Location A
Location B has no rocks or already sampled.
Sampling rocks at Location C
Location D has no rocks or already sampled.

Mars Environment (Before 2nd exploration):
Location A: No rocks
Location B: Rocks available
Location C: Rocks available
Location D: Rocks available

Rover starting exploration venture...
Location A has no rocks or already sampled.
Sampling rocks at Location B
Location C has no rocks or already sampled.
Sampling rocks at Location D

Rover Performance Summary:
Total samples collected: 4
Locations sampled: Location A, Location C, Location B, Location D
```

> Output varies each run due to the random environment initialisation.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x (no external libraries required — uses only the built-in `random` module)

### Run the simulation

```bash
# Clone the repository
git clone https://github.com/your-username/Autonomous-Mars-Rover-Exploration-Sim.git
cd Autonomous-Mars-Rover-Exploration-Sim

# Run the simulation
python Autonomous-Mars-Rover-Exploration-Sim.py
```

---

## 🧠 Concepts Demonstrated

| Concept | Implementation |
|---|---|
| **Intelligent Agent Design** | `RoverAgent` perceives environment state and acts autonomously |
| **Agent Memory / State** | `sampled_locations` set persists across exploration rounds |
| **Dynamic Environment** | `change_environment()` re-randomises conditions between rounds |
| **Simple Reflex + State** | Rover makes rule-based decisions informed by internal state |
| **Performance Measurement** | `samples_collected` counter tracks agent effectiveness |
| **Separation of Concerns** | Environment, agent logic, and simulation control are cleanly separated into 3 classes |

---

## 🔭 Possible Extensions

- **Grid-based map** — Replace named locations with an `(x, y)` coordinate grid for spatial navigation
- **Energy/battery system** — Add a fuel constraint that limits how many locations the rover can visit per round
- **Pathfinding** — Implement BFS or A* to find optimal exploration routes
- **Obstacle detection** — Add hazard tiles the rover must detect and avoid
- **Multiple rovers** — Simulate a fleet of agents with coordination logic
- **More environment events** — Add dust storms, temperature readings, or slope conditions
- **Data logging** — Export exploration results to CSV or JSON for analysis
- **Visualisation** — Use `matplotlib` or `pygame` to render the grid and rover movement in real time

---

## 👤 Author

**Stephen**

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
