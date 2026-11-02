"""
Example usage for Cutaneous Microcirculation & Laser Doppler Skill.
Demonstrates analyzing cutaneous local thermal hyperemia (LTH) test parameters.
"""

from client import CutaneousMicrocirculationClient


def main():
    client = CutaneousMicrocirculationClient()

    print("=== 1. Evaluating Cutaneous Local Thermal Hyperemia ===")
    res = client.evaluate_thermal_hyperemia(
        baseline_flux_pu=16.0,
        axon_peak_flux_pu=88.0,
        plateau_flux_pu=152.0,
        maximal_flux_pu=168.0,
        mean_arterial_pressure_mmhg=92.0
    )
    print(f"Mean Arterial Pressure: {res['mean_arterial_pressure_mmhg']} mmHg")
    print(f"CVC Baseline: {res['cvc_baseline']} | CVC Axon Peak: {res['cvc_axon_peak']} | CVC Plateau: {res['cvc_plateau']}")
    print(f"Axon Reflex Ratio: {res['axon_reflex_ratio']}x")
    print(f"%CVCmax Plateau: {res['pct_cvc_max_plateau']} %")
    print(f"Microvascular Reserve: {res['microvascular_reserve_ratio']}x over baseline")
    print(f"Endothelial Health Score: {res['endothelial_microvascular_health_score']} / 100")
    print(f"Classification: {res['classification']}")
    print(f"Interpretation: {res['physiological_interpretation']}")
    print(f"Actionable Guidance: {res['actionable_guidance']}")


if __name__ == "__main__":
    main()
