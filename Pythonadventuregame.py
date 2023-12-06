import streamlit as st

def main():
    # Initializing session states for each step of the game
    if 'name_entered' not in st.session_state:
        st.session_state['name_entered'] = False
    if 'direction_chosen' not in st.session_state:
        st.session_state['direction_chosen'] = False
    if 'left_path_taken' not in st.session_state:
        st.session_state['left_path_taken'] = False

    st.title("Welcome to the World of Vardheim")

    # Character name input
    if not st.session_state['name_entered']:
        name = st.text_input("Enter your Character's name: ")
        if name:
            st.session_state['name_entered'] = True
            st.write("Welcome", name, "to the World of Vardheim")

    # Choose direction
    if st.session_state['name_entered'] and not st.session_state['direction_chosen']:
        direction = st.radio("You have the option to go left or right, which way do you travel?", ('Left', 'Right'))

        if direction:
            st.session_state['direction_chosen'] = True
            st.session_state['direction'] = direction

    # Left path options
    if st.session_state['direction_chosen'] and st.session_state['direction'] == 'Left' and not st.session_state['left_path_taken']:
        left_path = st.button('Enter Elwynn Forest')
        if left_path:
            st.session_state['left_path_taken'] = True

    if st.session_state['left_path_taken']:
        defeat_defias = st.radio("You have entered Elwynn Forest. Do you want to take down the Defias Brotherhood?", ('Yes', 'No'))

        if defeat_defias == 'Yes':
            st.write("Congratulations, you are victorious!")
        elif defeat_defias == 'No':
            st.write("Congratulations, you accidentally stumble into BlackRock Mountain and were consumed by Ragnaros the Firelord.")
        else:
            st.write("You've made a grave miscalculation. The Defias Brotherhood sought you out and ended you")

    # Right path
    if st.session_state['direction_chosen'] and st.session_state['direction'] == 'Right':
        if st.button('Travel right from Elwynn Forest'):
            st.write("You make a right turn from Elwynn Forest and make your way into the Redridge Mountains")

if __name__ == "__main__":
    main()

