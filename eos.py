import streamlit as st
from streamlit_option_menu import option_menu

#..defining my function...
def eos_auto():           #...below is the horizontal menu 
    selected = option_menu(
        menu_title = 'Spot',
        options=['Deposit', 'Withdraw', 'Send','Transfer','Spot Account Statement','More'],
        menu_icon = 'cast',
        default_index=0,orientation='horizontal'
    )
#..automating address,network and memo only on EOS...
    cryptos = ['USDT','BTC','ETH','DOT','EOS','ADEX','APT','APX','BAR','BOBO']  #..crypto list..
    if selected == 'Send':
        crypto = st.selectbox('###### Crypto',cryptos)  #.. crypto selectbox after clicking send....
        if crypto == 'EOS':
            address = st.text_area('##### Address:',height=30, value='mexceosstart')
            network = st.text_area('##### Network:',height=30, value='EOS')
            memo = st.text_area('###### Memo/Tag:',height=30)
        else:
            address = st.text_area('###### Address:',height=30)
            network = st.text_area('###### Network:',height=30)
            memo = st.text_area('###### Memo/Tag:',height=30)
            
            
        ('---')
                
        #st.write(f"##### Crypto: {crypto}")
        #st.write(f"##### Address: {address}")
        #st.write(f"##### Network: {network}")
        #st.write(f"##### Memo/Tag: {memo}")
#st.write(eos_auto())
eos_auto()
