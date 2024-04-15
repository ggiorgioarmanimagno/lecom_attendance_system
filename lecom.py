import streamlit as st

st.title('Attendance System')

server_names = ['Sis Jenny', 'Sis Sylvia', 'Bro Bryan', 'Bro Gio']
selected_server_name = st.selectbox('Server Name:', server_names)

mass_type = ['Weekday Mass', 'Sunday Mass']
selected_mass_type = st.selectbox('Mass Type:', mass_type)

if selected_mass_type == 'Weekday Mass':
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    selected_day = st.selectbox('Mass Day:', days)

    schedules = ['6:15 AM', '7:00 AM', '6:00 PM']
    selected_schedule = st.selectbox('Mass Schedule', schedules)
else:
    days = ['Sunday']
    selected_day = st.selectbox('Day:', days)

    schedules = ['6:15 AM', '7:30 AM', '8:45 PM', '10:00 AM', '4:15 PM', '5:30 PM', '6:45 PM']
    selected_schedule = st.selectbox('Mass Schedule', schedules)

remarks = st.text_input('Remarks:')

submit_button = st.button("Log Attendance", use_container_width=True)

if submit_button:
    success_message = f"Attendance logged successfully for {selected_server_name}"
    st.write(f'<span style="color:green; font-weight:bold;">{success_message}</span>', unsafe_allow_html=True)
