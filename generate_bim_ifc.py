import json

def generate_ifc_structure():
    """
    Converts structural analysis output into a BIM IFC representation.
    """
    # Load analysis results
    try:
        with open("structural_output.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: Run structural_analysis.py first!")
        return

    # Mock IFC Structure Object
    ifc_model = {
        "IFC_Version": "IFC4",
        "Project_Name": "Automated Structural Beam Design",
        "Entity": "IfcBeam",
        "Properties": {
            "Length": f"{data['length_m']} m",
            "DesignLoad": f"{data['design_load_kN_m']} kN/m",
            "MaxMoment": f"{data['max_bending_moment_kNm']} kNm",
            "Status": data['status']
        }
    }

    # Save mock IFC-data structure
    with open("model.ifc", "w") as f:
        json.dump(ifc_model, f, indent=4)
        
    print("✅ Successfully generated BIM IFC Data payload (model.ifc)!")

if __name__ == "__main__":
    generate_ifc_structure()
