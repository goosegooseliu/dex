import streamlit as st

st.title('🎈 App Name')

st.write('Hello world!')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)
