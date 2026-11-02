"""
MCP Server for Cutaneous Microcirculation & Laser Doppler Thermal Hyperemia.
Exposes JSON-RPC endpoints for Cutaneous Vascular Conductance (CVC) and endothelial function scoring.
"""

import json
import sys
from client import CutaneousMicrocirculationClient

client = CutaneousMicrocirculationClient()


def handle_request(request: dict) -> dict:
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "evaluate_thermal_hyperemia",
                        "description": "Evaluates cutaneous laser Doppler thermal hyperemia kinetics, computing CVC, axon-reflex peak, NO plateau, and endothelial microvascular health score.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "baseline_flux_pu": {"type": "number", "description": "Baseline cutaneous perfusion units (PU) before heating"},
                                "axon_peak_flux_pu": {"type": "number", "description": "Initial sensory axon-reflex peak flux (PU) around 3-5 min"},
                                "plateau_flux_pu": {"type": "number", "description": "Secondary sustained endothelial NO plateau flux (PU) around 20-30 min"},
                                "maximal_flux_pu": {"type": "number", "description": "Maximal flux (PU) reached at 44 deg C heating or sodium nitroprusside"},
                                "mean_arterial_pressure_mmhg": {"type": "number", "description": "Subject mean arterial pressure (MAP = DBP + 1/3 PP) in mmHg"}
                            },
                            "required": ["baseline_flux_pu", "axon_peak_flux_pu", "plateau_flux_pu", "maximal_flux_pu", "mean_arterial_pressure_mmhg"]
                        }
                    }
                ]
            }
        }

    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})

        if tool_name == "evaluate_thermal_hyperemia":
            res = client.evaluate_thermal_hyperemia(
                baseline_flux_pu=args.get("baseline_flux_pu", 15.0),
                axon_peak_flux_pu=args.get("axon_peak_flux_pu", 85.0),
                plateau_flux_pu=args.get("plateau_flux_pu", 140.0),
                maximal_flux_pu=args.get("maximal_flux_pu", 155.0),
                mean_arterial_pressure_mmhg=args.get("mean_arterial_pressure_mmhg", 90.0)
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
            }

        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Method {tool_name} not found"}
            }

    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32600, "message": "Invalid Request"}
    }


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
