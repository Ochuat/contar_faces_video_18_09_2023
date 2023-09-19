# contar_faces_video_18_09_2023

# Relatório Técnico do Projeto de Detecção de Faces

## Introdução

### Problema de Processamento de Imagem Escolhido
O problema escolhido foi o de detecção e contagem de faces em um vídeo em tempo real.

### Justificativa
A detecção de faces é um dos problemas fundamentais em visão computacional e tem várias aplicações práticas, desde segurança até interfaces homem-máquina.

### Objetivo do Projeto
O objetivo deste projeto é desenvolver um sistema que seja capaz de contar o número de faces presentes em cada frame de um vídeo em tempo real.

### Link para Acesso ao Projeto
[[GitHub do Projeto](https://github.com/seu_usuario/seu_projeto)](https://github.com/Ochuat/contar_faces_video_18_09_2023)

## Desenvolvimento

### Algoritmo de Visão Computacional Usado
O algoritmo utilizado foi o Haar Cascade, que está integrado na biblioteca OpenCV.

### Fases do Desenvolvimento do Sistema
1. Inicialização do detector de faces (Haar Cascade)
2. Captura de vídeo em tempo real ou de um arquivo
3. Detecção de faces em cada frame
4. Contagem de faces
5. Exibição do resultado em tempo real

### Detalhes de Implementação
- Bibliotecas: OpenCV (`cv2`)
- Funções Específicas: `CascadeClassifier`, `VideoCapture`, `cvtColor`, `detectMultiScale`, `rectangle`, `putText`

## Resultados

### Resultado Final
O sistema consegue detectar e contar o número de faces presentes em cada frame de um vídeo em tempo real.

### Como Usar o Sistema
Execute o script Python e o vídeo será reproduzido com um retângulo verde ao redor das faces detectadas. O número de faces também será exibido.

## Conclusão
O projeto foi bem-sucedido na detecção e contagem de faces em tempo real. Isso tem várias aplicações práticas, desde segurança até análise de comportamento.

### Possíveis Aplicações e Usos
1. Monitoramento de segurança
2. Análise de comportamento em ambientes públicos

### Sugestões para Futuras Melhorias
1. Implementar detecção em tempo real através de uma câmera ao vivo
2. Melhorar a eficiência do algoritmo para funcionar em dispositivos de baixa potência

## Referências
- OpenCV Documentation
- Haar Cascades: A Comprehensive Study
