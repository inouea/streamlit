import streamlit as st
# import numpy as np
# import pandas as pd 
# from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです。')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

# text = st.text_input('あなたの趣味を教えて下さい。',)
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味:', text
# 'コンディション：', condition

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='11月度データ', use_column_width=True)



# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, str50] + [35.69, 139.70],
#     columns = ['lat', 'lon']
# )

#st.dataframe(df.style.highlight_max(axis=0) )
# st.map(df)

# """
# # 章
# ## 説
# ### 項

# ```python
# import streamlit as st
# import numpy as numpy
# import pandas as pd 
# ```
 
# """


