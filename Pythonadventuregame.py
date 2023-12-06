import streamlit as st

def main():
    st.title("Welcome to the World of Vardheim")

    # Character name input
    name = st.text_input("Enter your Character's name: ")
    if name:
        st.write("Welcome", name, "to the World of Vardheim")

        # Choose direction
        direction = st.radio("You are outside of Goldshire in Elywynn Forest. You have the option to go left or right, which way do you travel?", ('Left', 'Right'))

        if direction == 'Left':
            # Left path options
            left_path = st.button('Travel left')

            if left_path:
                # Encounter in Elwynn Forest
                st.write("You have entered Westfall.")
                defeat_defias = st.radio("Do you want to take down the Defias Brotherhood?", ('Yes', 'No'))

                if defeat_defias == 'Yes':
                    st.write("Congratulations, you are victorious!")
                elif defeat_defias == 'No':
                    st.write("Congratulations, you accidentally stumble into BlackRock Mountain and were consumed by Ragnaros the Firelord.")
                else:
                    st.write("You've made a grave miscalculation. The Defias Brotherhood sought you out and ended you")

        elif direction == 'Right':
            # Right path
            if st.button('Travel right'):
                st.write("You make a right turn from Elwynn Forest and make your way into the Redridge Mountains")

if __name__ == "__main__":
    main()
