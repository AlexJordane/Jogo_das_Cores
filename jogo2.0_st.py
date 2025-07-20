import streamlit as st
import random
from PIL import Image

def processar_clique(linha_clicada, coluna_clicada):
    st.session_state.numero_jogadas += 1
       
    if linha_clicada == 0 and coluna_clicada == 0:
        st.session_state.grid[0][0] = 1 - st.session_state.grid[0][0]
        st.session_state.grid[0][1] = 1 - st.session_state.grid[0][1]
        st.session_state.grid[1][0] = 1 - st.session_state.grid[1][0]

    elif linha_clicada == 0 and coluna_clicada == 1:
        st.session_state.grid[0][0] = 1 - st.session_state.grid[0][0]
        st.session_state.grid[0][1] = 1 - st.session_state.grid[0][1]
        st.session_state.grid[0][2] = 1 - st.session_state.grid[0][2]

    elif linha_clicada == 0 and coluna_clicada == 2:
        st.session_state.grid[1][2] = 1 - st.session_state.grid[1][2]
        st.session_state.grid[0][1] = 1 - st.session_state.grid[0][1]
        st.session_state.grid[0][2] = 1 - st.session_state.grid[0][2]
        
    elif linha_clicada == 1 and coluna_clicada == 0:
        st.session_state.grid[0][0] = 1 - st.session_state.grid[0][0]
        st.session_state.grid[1][0] = 1 - st.session_state.grid[1][0]
        st.session_state.grid[2][0] = 1 - st.session_state.grid[2][0]

    elif linha_clicada == 1 and coluna_clicada == 1:
        st.session_state.grid[0][1] = 1 - st.session_state.grid[0][1]
        st.session_state.grid[1][0] = 1 - st.session_state.grid[1][0]
        st.session_state.grid[1][1] = 1 - st.session_state.grid[1][1]
        st.session_state.grid[1][2] = 1 - st.session_state.grid[1][2]
        st.session_state.grid[2][1] = 1 - st.session_state.grid[2][1]

    elif linha_clicada == 1 and coluna_clicada == 2:
        st.session_state.grid[2][2] = 1 - st.session_state.grid[2][2]
        st.session_state.grid[1][2] = 1 - st.session_state.grid[1][2]
        st.session_state.grid[0][2] = 1 - st.session_state.grid[0][2]
        
    elif linha_clicada == 2 and coluna_clicada == 0:
        st.session_state.grid[2][0] = 1 - st.session_state.grid[2][0]
        st.session_state.grid[1][0] = 1 - st.session_state.grid[1][0]
        st.session_state.grid[2][1] = 1 - st.session_state.grid[2][1]
        
    elif linha_clicada == 2 and coluna_clicada == 1:
        st.session_state.grid[2][0] = 1 - st.session_state.grid[2][0]
        st.session_state.grid[2][1] = 1 - st.session_state.grid[2][1]
        st.session_state.grid[2][2] = 1 - st.session_state.grid[2][2]

    elif linha_clicada == 2 and coluna_clicada == 2:
        st.session_state.grid[2][2] = 1 - st.session_state.grid[2][2]
        st.session_state.grid[2][1] = 1 - st.session_state.grid[2][1]
        st.session_state.grid[1][2] = 1 - st.session_state.grid[1][2]
    
    st.session_state.conta_vermelhos = 0
    
    for linha in range(3):
        for coluna in range(3):
            st.session_state.conta_vermelhos += st.session_state.grid[linha][coluna]

    return 

def iniciar_partida():
    grid = [[random.randint(0, 1) for _ in range(3)] for _ in range(3)]
    st.session_state.numero_jogadas = 0
    st.session_state.conta_vermelhos = 0
    st.session_state.jogo_finalizado = False
    for linha in range(3):
        for coluna in range(3):
            st.session_state.conta_vermelhos += grid[linha][coluna]

    return grid

# Coloque este bloco de código, por exemplo, logo após a inicialização do session_state

# --- BARRA LATERAL COM AS REGRAS ---
with st.sidebar:
    st.title("🎨 Jogo das Cores")
    st.header("📜 Regras do Jogo")

    st.write("🎯 **Objetivo:**")
    st.error("O objetivo é **mudar a cor** de todos os quadrados do tabuleiro para **vermelho** (🟥).")
    
    st.write("🕹️ **Como Jogar:**")
    st.info("""
    - O jogo começa com alguns quadrados vermelhos (🟥) e outros azuis (🟦).
    - O padrão da mudança de cor depende da posição do quadrado em que você clica:
        - ⬛ Nos cantos: O clique inverte a cor do próprio quadrado e de seus dois vizinhos, formando um "L".
        - ⬜ Nos meios das bordas: O clique inverte a cor da linha ou coluna inteira à qual o quadrado pertence.
        - ╋ No centro: O clique inverte a cor do próprio quadrado e de seus quatro vizinhos, formando uma cruz.
    - Cada clique conta como uma jogada. Tente resolver o quebra-cabeça no menor número de jogadas possível!
    - A imagem abaixo ilustra as regras do jogo.
    """)

    image = Image.open("regras_jogo.png")
    st.sidebar.image(image, caption="Entenda as Regras!", use_container_width=True)

    st.write("🏆 **Vitória:**")
    st.success("O jogo termina quando todos os quadrados estiverem vermelhos. Os balões comemoram sua vitória!")
    
    st.write("🔄 **Recomeçar:**")
    st.warning("A qualquer momento, você pode clicar em 'Reiniciar Partida' para começar um novo desafio com um tabuleiro diferente.")


if 'jogo_finalizado' not in st.session_state:
    st.session_state.jogo_finalizado = False

if 'grid' not in st.session_state:
    st.session_state.grid = iniciar_partida()

st.header("🎨 Jogo das Cores")

col_info, col_acao = st.columns([2, 1]) # A primeira coluna é 2x maior que a segunda

with col_info:
    # Use a métrica para exibir as jogadas
    st.metric(label="Jogadas", value=st.session_state.numero_jogadas)

with col_acao:
    # Coloque seu botão de reiniciar aqui
    if st.button("Reiniciar Partida"):
        # Chame sua função de reinício e atualize o session_state
        st.session_state.grid = iniciar_partida()
        st.rerun() # Comando útil para forçar o recarregamento da tela

grid_atual = st.session_state.grid

for linha_idx in range(len(grid_atual)):
    spacer_esquerda, col1, col2, col3, spacer_direita = st.columns([3, 1, 1, 1, 3])
    colunas_do_grid = [col1, col2, col3]
    for col_idx in range(len(colunas_do_grid)):
        with colunas_do_grid[col_idx]:
            valor_quadrado = grid_atual[linha_idx][col_idx]
            if valor_quadrado == 0:
                emoji = '🟦'
            else:
                emoji = '🟥'
            st.button(
                emoji,
                key=f'btn_{linha_idx}_{col_idx}',
                on_click=processar_clique,  # <--- Aponta para a sua função
                args=(linha_idx, col_idx),   # <--- Passa a linha e coluna atuais como argumentos
                disabled=st.session_state.jogo_finalizado
                )

if 'conta_vermelhos' in st.session_state:
    if st.session_state.conta_vermelhos == 9:
        st.session_state.jogo_finalizado = True
        st.balloons() # Efeito de comemoração do Streamlit!
        st.success(f'Parabéns! Você ganhou o jogo com {st.session_state.numero_jogadas} jogadas!')
        st.info("Clique em 'Reiniciar Partida' para jogar de novo.")

    elif st.session_state.conta_vermelhos == 0:
        st.info('Você deixou todos os quadrados azuis! Agora o desafio é deixar todos vermelhos.')

    else:
        st.info(f'Você tem {st.session_state.conta_vermelhos} quadrados vermelhos. Continue jogando!')
