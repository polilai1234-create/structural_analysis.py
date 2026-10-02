import json

def analyze_beam(length_m, dead_load_knm, live_load_knm):
    """
    Automated Structural Analysis for a Simply Supported Beam
    Calculates factored design loads, max moment, max shear, and checks section status.
    """
    # Factored Load Combination (1.35 * DL + 1.5 * LL)
    w_u = (1.35 * dead_load_knm) + (1.5 * live_load_knm)
    
    # Structural Calculations
    max_moment_kNm = (w_u * (length_m ** 2)) / 8
    max_shear_kN = (w_u * length_m) / 2
    
    # BIM Structural Data Payload
    bim_data = {
        "element_type": "Structural Beam",
        "length_m": length_m,
        "design_load_kN_m": round(w_u, 2),
        "max_bending_moment_kNm": round(max_moment_kNm, 2),
        "max_shear_force_kN": round(max_shear_kN, 2),
        "status": "PASS" if max_moment_kNm < 500 else "RE-DESIGN REQUIRED"
    }
    
    return bim_data

if __name__ == "__main__":
    # Test Parameters
    result = analyze_beam(length_m=6.0, dead_load_knm=15.0, live_load_knm=10.0)
    print(json.dumps(result, indent=4))
    
    # Save output for BIM Pipeline
    with open("structural_output.json", "w") as f:
        json.dump(result, f, indent=4)
