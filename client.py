"""
Cutaneous Microcirculation & Laser Doppler Thermal Hyperemia Engine.
Provides deterministic, zero-dependency modeling of cutaneous vascular conductance (CVC),
sensory axon-reflex peak, endothelial nitric oxide plateau, and microvascular reserve.
"""

from typing import Dict, Any, List, Optional


class CutaneousMicrocirculationClient:
    """
    Deterministic client for analyzing cutaneous laser Doppler flowmetry and thermal hyperemia kinetics.
    Pure Python standard library implementation based on clinical microvascular protocols.
    """

    def __init__(self):
        pass

    def evaluate_thermal_hyperemia(
        self,
        baseline_flux_pu: float,
        axon_peak_flux_pu: float,
        plateau_flux_pu: float,
        maximal_flux_pu: float,
        mean_arterial_pressure_mmhg: float
    ) -> Dict[str, Any]:
        """
        Evaluates local thermal hyperemia response (heating to 42-43 deg C):
        - Calculates Cutaneous Vascular Conductance (CVC = Flux / MAP * 100).
        - Computes Axon Reflex Ratio and %CVC_max plateau.
        - Scores Endothelial Microvascular Health Score (EMHS, 0-100).
        """
        if mean_arterial_pressure_mmhg <= 40.0:
            return {"error": "Mean arterial pressure must be a valid physiological value (> 40 mmHg)"}

        map_val = mean_arterial_pressure_mmhg
        cvc_base = round((baseline_flux_pu / map_val) * 100.0, 3)
        cvc_axon = round((axon_peak_flux_pu / map_val) * 100.0, 3)
        cvc_plat = round((plateau_flux_pu / map_val) * 100.0, 3)
        cvc_max = round((maximal_flux_pu / map_val) * 100.0, 3)

        # Axon reflex ratio (sensory C-fiber neurogenic response)
        axon_ratio = round(cvc_axon / max(0.01, cvc_base), 2)

        # Plateau fraction relative to maximal pharmacologic or suprathermal vasodilation
        pct_cvc_max = round((cvc_plat / max(0.01, cvc_max)) * 100.0, 1)

        # Microvascular reserve (expansion over baseline)
        reserve_ratio = round(cvc_plat / max(0.01, cvc_base), 2)

        # Endothelial Microvascular Health Score (EMHS, 0 - 100):
        # Plateau >= 85% CVCmax is normal, axon ratio >= 4.0 is normal
        axon_score = min(40.0, (axon_ratio / 5.0) * 40.0)
        plateau_score = min(60.0, (pct_cvc_max / 90.0) * 60.0)
        emhs = round(min(100.0, max(5.0, axon_score + plateau_score)), 1)

        is_endothelial_blunted = pct_cvc_max < 70.0
        is_neurogenic_blunted = axon_ratio < 2.5

        if emhs >= 80.0:
            tier = "OPTIMAL_MICROVASCULAR_FUNCTION"
            interpretation = "Robust sensory C-fiber axon reflex and intact nitric oxide-mediated endothelial vasodilation."
            recommendation = "Microcirculatory perfusion is exceptional. Maintain aerobic conditioning and vascular health."
        elif is_neurogenic_blunted and not is_endothelial_blunted:
            tier = "ISOLATED_NEUROGENIC_ATTENUATION"
            interpretation = "Sub-optimal sensory axon reflex with preserved endothelial NO plateau. Screen for peripheral sensory neuropathy."
            recommendation = "Review glucose tolerance, vitamin B12 status, and avoid prolonged local thermal or compressive stress."
        elif is_endothelial_blunted:
            tier = "MICROVASCULAR_ENDOTHELIAL_DYSFUNCTION"
            interpretation = "Attenuated thermal plateau indicates impaired microvascular endothelial NO bio-availability."
            recommendation = "Prioritize dietary dietary nitrate intake (beetroot, arugula), Zone 2 exercise, and reduce systemic oxidative stress."
        else:
            tier = "MODERATE_MICROVASCULAR_RESERVE"
            interpretation = "Mildly reduced thermal hyperemia kinetics across both sensory and endothelial phases."
            recommendation = "Engage in contrast hydrotherapy or sauna exposure to stimulate microcirculatory shear stress adaptations."

        return {
            "mean_arterial_pressure_mmhg": map_val,
            "cvc_baseline": cvc_base,
            "cvc_axon_peak": cvc_axon,
            "cvc_plateau": cvc_plat,
            "cvc_maximal": cvc_max,
            "axon_reflex_ratio": axon_ratio,
            "pct_cvc_max_plateau": pct_cvc_max,
            "microvascular_reserve_ratio": reserve_ratio,
            "endothelial_microvascular_health_score": emhs,
            "classification": tier,
            "physiological_interpretation": interpretation,
            "actionable_guidance": recommendation
        }
