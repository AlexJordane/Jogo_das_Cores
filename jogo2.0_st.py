import streamlit as st
import random
import numpy as np

def gerar_tom(frequencia, duracao=1.0):
    taxa_amostragem = 44100
    amplitude = 4096
    tempo = np.linspace(0, duracao, int(taxa_amostragem * duracao), False)
    onda = amplitude * np.sin(frequencia * tempo * 2 * np.pi)
    onda_formatada = onda.astype(np.int16)
    som_estereo = np.c_[onda_formatada, onda_formatada]
    som_final = pygame.sndarray.make_sound(som_estereo)
    return som_final

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

def som_vitoria(fim):
    # Você pode definir uma velocidade base para a música
    tempo_base = 0.12

    tempo_base_animado = 0.09


    fanfarra_vermelha = [
        # Parte 1: A corrida inicial que cria expectativa
        (392.00, tempo_base_animado),       # Sol (G4)
        (440.00, tempo_base_animado),       # Lá (A4)
        (493.88, tempo_base_animado),       # Si (B4)
        (523.25, tempo_base_animado * 2),   # Dó (C5) - um pouco mais longa

        # Parte 2: O salto e o pico de energia
        (783.99, tempo_base_animado * 4),   # Sol agudo (G5) - nota alta e longa

        # Parte 3: A descida rítmica e "saltitante"
        (659.25, tempo_base_animado * 2),   # Mi agudo (E5)
        (0, tempo_base_animado),            # Pequena pausa
        (587.33, tempo_base_animado * 2),   # Ré agudo (D5)
        (0, tempo_base_animado),            # Pequena pausa
        (523.25, tempo_base_animado * 3),   # Dó agudo (C5) - nota de resolução

        # Parte 4: O acorde final, rápido e triunfante
        (0, tempo_base_animado * 2),        # Pausa antes do fim
        (392.00, tempo_base_animado),       # Sol (G4)
        (523.25, tempo_base_animado),       # Dó agudo (C5)
        (659.25, tempo_base_animado),       # Mi agudo (E5)
        (783.99, tempo_base_animado * 4)    # Sol agudo (G5) - A grande nota final
    ]


    # A sequência de notas da nossa fanfarra
    fanfarra_azul = [
        # 1. A subida do arpejo
        (261.63, tempo_base),      # Dó (C4)
        (329.63, tempo_base),      # Mi (E4)
        (392.00, tempo_base),      # Sol (G4)

        # 2. O pico triunfante
        (523.25, tempo_base * 3),  # Dó agudo (C5), nota mais longa

        # 3. A pausa dramática
        (0, tempo_base * 2),       # Silêncio

        # 4. A resolução final (um acorde que soa vitorioso)
        (392.00, tempo_base),      # Sol (G4)
        (523.25, tempo_base),      # Dó agudo (C5)
        (659.25, tempo_base * 2)   # Mi mais agudo (E5), nota final longa
    ]
    if fim:
        fanfarra_vitoria = fanfarra_vermelha
    else:
        fanfarra_vitoria = fanfarra_azul

    for nota in fanfarra_vitoria:
        if nota[0] == 0:
            pygame.time.wait(int(nota[1]*1000))
        else:
            tocar = gerar_tom(frequencia=nota[0], duracao=nota[1])
            tocar.play()
            pygame.time.wait(int(nota[1] * 1000))

def iniciar_partida():
    grid = [[random.randint(0, 1) for _ in range(3)] for _ in range(3)]
    st.session_state.numero_jogadas = 0
    st.session_state.conta_vermelhos = 0
    st.session_state.jogo_finalizado = False
    for linha in range(3):
        for coluna in range(3):
            st.session_state.conta_vermelhos += grid[linha][coluna]

    return grid

if 'jogo_finalizado' not in st.session_state:
    st.session_state.jogo_finalizado = False

if 'grid' not in st.session_state:
    st.session_state.grid = iniciar_partida()

st.header("Jogo das Cores")

col_info, col_acao = st.columns([2, 1]) # A primeira coluna é 2x maior que a segunda

if 'conta_vermelhos' in st.session_state:
    if st.session_state.conta_vermelhos == 9:
        st.session_state.jogo_finalizado = True
        st.balloons() # Efeito de comemoração do Streamlit!
        st.success(f'Parabéns! Você ganhou o jogo com {st.session_state.numero_jogadas} jogadas!')
        st.info("Clique em 'Reiniciar Partida' para jogar de novo.")

    elif st.session_state.conta_vermelhos == 0:
        st.info('Você deixou todos os quadrados azuis! Agora o desafio é deixar todos vermelhos.')

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

# 1. Itera por cada NÚMERO DE LINHA (0, 1, 2)
for linha_idx in range(len(grid_atual)):

    # 2. Para cada linha, cria 3 contêineres de coluna
    spacer_esquerda, col1, col2, col3, spacer_direita = st.columns([3, 1, 1, 1, 3])

    colunas_do_grid = [col1, col2, col3]


    # 3. Itera por cada NÚMERO DE COLUNA (0, 1, 2)
    for col_idx in range(len(colunas_do_grid)):

        # 4. Acessa o contêiner da coluna específica (0, 1 ou 2)
        with colunas_do_grid[col_idx]:
            
            # 5. Decide qual emoji ("cor") usar com base no estado guardado
            valor_quadrado = grid_atual[linha_idx][col_idx]
            if valor_quadrado == 0:
                emoji = '🟦'
            else:
                emoji = '🟥'
            
            # 6. Cria o botão!
            #    - O texto do botão é o emoji.
            #    - A 'key' é uma string única para este botão específico.

            st.button(
                emoji,
                key=f'btn_{linha_idx}_{col_idx}',
                on_click=processar_clique,  # <--- Aponta para a sua função
                args=(linha_idx, col_idx),   # <--- Passa a linha e coluna atuais como argumentos
                disabled=st.session_state.jogo_finalizado
                )

