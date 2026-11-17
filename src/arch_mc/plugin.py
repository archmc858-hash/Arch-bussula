from endstone.event import PlayerChatEvent, event_handler
from endstone.form import ActionForm
from endstone.plugin import Plugin


class ArchMCPlugin(Plugin):
    """Initial menu and chat-alias foundation for ARCH MC."""

    api_version = "0.11"
    prefix = "ARCH MC"

    def on_enable(self) -> None:
        self.register_events(self)
        self.logger.info("ARCH MC plugin base enabled.")

    @event_handler
    def on_player_chat(self, event: PlayerChatEvent) -> None:
        message = event.message.strip()
        if not message.startswith("!"):
            return

        player = event.player
        command = message.lower().split()[0]

        routes = {
            "!menu": self.show_main_menu,
            "!spawn": lambda p: self.teleport_notice(p, "Spawn"),
            "!arena": lambda p: self.teleport_notice(p, "Arena Solaris"),
            "!clan": self.show_clan,
            "!troca": self.show_trade,
            "!homes": self.show_homes,
        }

        handler = routes.get(command)
        if handler is None:
            return

        event.is_cancelled = True
        handler(player)

    def show_main_menu(self, player) -> None:
        form = ActionForm(title="ARCH MC", content="Selecione um sistema:")
        form.add_button("Teleportes", on_click=lambda p: self.show_teleports(p))
        form.add_button("Homes", on_click=lambda p: self.show_homes(p))
        form.add_button("Clã", on_click=lambda p: self.show_clan(p))
        form.add_button("Trocas", on_click=lambda p: self.show_trade(p))
        player.send_form(form)

    def show_teleports(self, player) -> None:
        form = ActionForm(title="Teleportes", content="Escolha o destino:")
        form.add_button("Spawn", on_click=lambda p: self.teleport_notice(p, "Spawn"))
        form.add_button("Arena Solaris", on_click=lambda p: self.teleport_notice(p, "Arena Solaris"))
        form.add_button("Voltar", on_click=self.show_main_menu)
        player.send_form(form)

    def show_homes(self, player) -> None:
        form = ActionForm(
            title="Homes",
            content="A interface está criada. A próxima etapa implementará criação, edição, exclusão e teleporte das homes com salvamento por jogador."
        )
        form.add_button("Voltar", on_click=self.show_main_menu)
        player.send_form(form)

    def show_clan(self, player) -> None:
        form = ActionForm(
            title="Clã",
            content="A interface está criada. A próxima etapa implementará criação de clãs, convites, entrada, saída e permissões de liderança."
        )
        form.add_button("Voltar", on_click=self.show_main_menu)
        player.send_form(form)

    def show_trade(self, player) -> None:
        form = ActionForm(
            title="Trocas",
            content="A interface está criada. A próxima etapa implementará convites e troca real de itens, com confirmação dupla e cancelamento seguro."
        )
        form.add_button("Voltar", on_click=self.show_main_menu)
        player.send_form(form)

    def teleport_notice(self, player, destination: str) -> None:
        player.send_message(
            f"§e[ARCH MC] §f{destination} ainda precisa ter suas coordenadas configuradas pelo administrador."
        )
