import streamlit as st

def render_emergency_form():
    """
    Render the emergency situation form.
    
    Returns:
        Dictionary with form data
    """
    with st.form("emergency_form"):
        # Situation description
        situation = st.text_area(
            "Describe the emergency situation",
            placeholder="Provide details about what happened...",
            help="Be specific about the situation to get the most relevant guidance"
        )
        
        # Emergency type
        emergency_types = [
            "Select emergency type",
            "Bleeding/Wounds",
            "Burns",
            "Cardiac Emergency",
            "Choking",
            "Fractures/Sprains",
            "Head Injury",
            "Heat/Cold Emergency",
            "Poisoning",
            "Seizure",
            "Shock",
            "Other Medical Emergency",
            "Natural Disaster",
            "Fire Emergency",
            "Water Emergency"
        ]
        
        emergency_type = st.selectbox(
            "Type of Emergency",
            options=emergency_types
        )
        
        # Additional details
        col1, col2 = st.columns(2)
        
        with col1:
            severity = st.select_slider(
                "Severity",
                options=["Low", "Medium", "High"],
                value="Medium"
            )
            
        with col2:
            age_group = st.selectbox(
                "Age Group",
                options=["Infant (0-1)", "Child (1-12)", "Teen (13-17)", "Adult (18-65)", "Elderly (65+)"],
                index=3
            )
        
        # Submit button
        submit_button = st.form_submit_button("Get Emergency Guidance", type="primary")
        
        if submit_button:
            if emergency_type == "Select emergency type":
                st.error("Please select an emergency type")
                return None
            
            if not situation or len(situation.strip()) < 10:
                st.error("Please provide more details about the situation (description too short)")
                return None
            
            return {
                "situation": situation,
                "emergency_type": emergency_type,
                "severity": severity.lower(),
                "age_group": age_group
            }
        
        return None