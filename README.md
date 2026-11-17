# ARCH MC — Plugin base (Endstone 0.11.16)

Este pacote é a **primeira base de desenvolvimento**, não é ainda o sistema final completo.

## O que esta versão já contém
- Estrutura de pacote Python para Endstone 0.11.x.
- Plugin principal `ArchMCPlugin`.
- Menu Bedrock com botões de texto: Teleportes, Homes, Clã e Trocas.
- Atalhos no chat: `!menu`, `!spawn`, `!arena`, `!homes`, `!clan`, `!troca`.
- As telas de Homes, Clã e Trocas estão identificadas como etapas seguintes; ainda não movimentam dados ou itens.
- Spawn e Arena Solaris ainda precisam das coordenadas reais do ARCH MC.

## Importante
Não instale esta versão no servidor principal como se estivesse pronta. Ela serve para validar a estrutura e a abertura dos menus. Antes de ativar no ARCH MC, vamos implementar e testar:
1. Coordenadas/dimensões de Spawn e Arena Solaris.
2. Abertura do menu ao interagir com a bússola.
3. Homes persistentes por jogador.
4. Clãs, convites e permissões.
5. Trocas reais de itens com confirmação dupla, validação de inventário e cancelamento seguro.

## Estrutura
```text
ARCH_MC_Plugin_Starter/
├── pyproject.toml
├── README.md
└── src/
    └── arch_mc/
        ├── __init__.py
        └── plugin.py
```

## Build
Com Python e Endstone 0.11.16 instalados:
```bash
python -m pip install build
python -m build
```
O arquivo `.whl` será criado em `dist/`.

A instalação no servidor deve ser feita somente depois de validar o pacote em um servidor de teste/backup.
