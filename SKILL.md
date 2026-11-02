---
name: genpark-personal-agent-cutaneous-microcirculation-laser-doppler-skill
description: Deterministic evaluation of cutaneous microcirculation, laser Doppler thermal hyperemia, sensory axon reflex, and endothelial nitric oxide capacity.
version: 1.0.0
author: GenPark Autonomous Agents Ecosystem
license: MIT
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
---

# Cutaneous Microcirculation & Laser Doppler Thermal Hyperemia Skill

## Overview
The `genpark-personal-agent-cutaneous-microcirculation-laser-doppler-skill` equips personal sovereign agents with non-invasive microvascular assessment tools. Cutaneous circulation provides a direct, accessible window into systemic microvascular endothelial health. Applying controlled local heating (42-43°C) elicits a biphasic vasodilatory response: an initial sensory C-fiber axon reflex peak followed by a prolonged plateau mediated 65-70% by endothelial Nitric Oxide (NO) synthase. This skill calculates Cutaneous Vascular Conductance (CVC), compares plateau dilation against maximal physiological capacity, and scores overall microvascular resilience.

## Physiological Model & Mathematics
1. **Cutaneous Vascular Conductance ($CVC$)**:
   $$CVC = \frac{\text{Laser Doppler Flux (PU)}}{\text{Mean Arterial Pressure (mmHg)}} \times 100$$
2. **Axon Reflex Peak Ratio ($ARR$)**:
   $$ARR = \frac{CVC_{\text{axon\_peak}}}{CVC_{\text{baseline}}}$$
   - Evaluates unmyelinated C-fiber neurogenic flare (substance P / CGRP release).
3. **Endothelial Plateau (%$CVC_{\max}$)**:
   $$\%CVC_{\max} = \frac{CVC_{\text{plateau}}}{CVC_{\max}} \times 100\%$$
   - Normative physiological benchmark: $\ge 85 - 90\%$.
   - Reductions ($< 70\%$) reflect impaired endothelial nitric oxide bio-availability and microvascular rarefaction.
4. **Endothelial Microvascular Health Score ($EMHS$)**:
   Integrates neurogenic axon reflex power and sustained endothelial NO reserve into a 0 to 100 index.

## Tools & Endpoints
- `evaluate_thermal_hyperemia`: Computes baseline, peak, and plateau CVC, axon ratio, $\%CVC_{\max}$, and endothelial health score.
