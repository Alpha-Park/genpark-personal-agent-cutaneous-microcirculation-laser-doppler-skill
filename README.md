# Cutaneous Microcirculation & Laser Doppler Thermal Hyperemia Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen.svg)](https://github.com/alphaparkinc/genpark-personal-agent-cutaneous-microcirculation-laser-doppler-skill)
[![OpenClaw Ready](https://img.shields.io/badge/OpenClaw-Compatible-purple.svg)](https://github.com/alphaparkinc/genpark-personal-agent-cutaneous-microcirculation-laser-doppler-skill)
[![MCP Protocol](https://img.shields.io/badge/MCP-Standard-orange.svg)](https://modelcontextprotocol.io/)

A sovereign personal agent capability for computational microvascular assessment, evaluating cutaneous laser Doppler flowmetry, sensory C-fiber axon reflexes, and endothelial nitric oxide capacity.

## Architecture

```mermaid
flowchart TD
    LaserDoppler["Laser Doppler Flux (PU) & MAP (mmHg)"] --> CVC["Cutaneous Vascular Conductance (CVC = Flux / MAP * 100)"]
    CVC --> Phase1["Initial Sensory Axon Reflex Peak (C-Fiber Neuropeptides)"]
    CVC --> Phase2["Sustained Plateau (Endothelial Nitric Oxide / EETs)"]
    Phase1 & Phase2 --> Metrics["Axon Ratio & %CVC_max Plateau"]
    Metrics --> EMHS["Endothelial Microvascular Health Score (0 - 100)"]
    EMHS --> AgentDirectives["OpenClaw / Hermes Cardiovascular & Dietary Nitrate Guidance"]
```

## Quickstart

```python
from client import CutaneousMicrocirculationClient

client = CutaneousMicrocirculationClient()

# Assess cutaneous local thermal hyperemia
res = client.evaluate_thermal_hyperemia(
    baseline_flux_pu=16.0,
    axon_peak_flux_pu=88.0,
    plateau_flux_pu=152.0,
    maximal_flux_pu=168.0,
    mean_arterial_pressure_mmhg=92.0
)

print("%CVCmax Plateau:", res["pct_cvc_max_plateau"], "%")
print("Axon Reflex Ratio:", res["axon_reflex_ratio"], "x")
print("Microvascular Health Score:", res["endothelial_microvascular_health_score"], "/ 100")
print("Classification:", res["classification"])
```

## MCP Server Integration

Add to your `claude_desktop_config.json` or OpenClaw tool registry:

```json
{
  "mcpServers": {
    "cutaneous-microcirculation": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-cutaneous-microcirculation-laser-doppler-skill/mcp_server.py"]
    }
  }
}
```

## License
MIT License.
