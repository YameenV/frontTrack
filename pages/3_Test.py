import streamlit as st

def Test():
    st.title("Test User")

    st.multiselect("Select user to Perform test", ["test", "run", "main"])

    st.multiselect("Select the type of test to Perform",["test", "run", "main"])

if __name__ == "__main__":
    if st.session_state["authentication_status"]:
        Test()
    else:
        st.warning("Logging to acess the page")