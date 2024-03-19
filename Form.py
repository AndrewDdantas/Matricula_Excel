import streamlit as st
import pandas as pd 

base = pd.read_excel('./BASE ALUNOS.xlsx')

id_func = st.selectbox('Qual seu ID ?', base['ID'].unique())


st.write(st.secrets['db_username'])

base_fil = base[base['ID'] == id_func]

nome = base_fil.pop('NOME').iloc[0]

st.markdown(f'Olá {nome} !')

if base_fil['RESPOSTA'].notnull().any():
    st.write('Você já respondeu esse formulário!')

else:
    with st.form("formulario_perguntas"):
        respostas = {}

        for index, row in base_fil.iterrows():
            # Criar botões de rádio para cada pergunta
            resposta = st.radio(row['PERGUNTA'], ['Sim', 'Não'], key=index)
            respostas[row['PERGUNTA']] = resposta
            
        submitted = st.form_submit_button("Enviar")
        if submitted:
            # Processar as respostas
            for pergunta, resposta in respostas.items():
                st.write("Resposta registrada com sucesso!")
                indices = base[base['ID'] == id_func].index
                for indice in indices:
                    base.at[indice, 'RESPOSTA'] = resposta

base.to_excel('./BASE ALUNOS.xlsx', index=False)


