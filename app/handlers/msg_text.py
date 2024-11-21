from loader import _

# Текста было много и он повторялся. 
# По этой причине вынеc в отдельный файл :)

class MsgText:
    @property
    def WELCOME(self):
        return _("👋, <a href='tg://user?id={}'>{}</a>")
    @property
    def CHANGE_LANG(self):
        return _("Выберите язык, на который вы хотите переключиться: 🌐")
    
    @property
    def DONE_CHANGE_LANG(self):
        return _("Ваш язык успешно изменён! ✅")
    
    @property
    def WALLET(self):
        return _("У тебя - <code>{}$</code> 🐽")
    
    @property
    def FARM(self):
        return _("Вы получили <code>{}$</code> 🐽")
    
    @property
    def FARM_COOLDOWN(self):
        return _("Зай тише будь...\nСледующая добыча через {}ч {}м {}с.")

    @property
    def CHANCES(self):
        return _("Заюш думаю, что вероятность {}% 👯‍♂️")
    
    @property
    def SHIP(self):
        return _("<blockquote>{}</blockquote> 💞 <blockquote>{}</blockquote>\n\nLюбov рильно")
    
    @property
    def WHO(self):
        return _("💫✨Звезды шепчут, что <code>{}</code> {}")
    
    @property
    def HELP(self):
        return _("""
Ферма – собирай монеты (1–60) раз в 6 часов.
Шура кто... – выбирает из предложенных вариантов. 
Шура инфа... – показывает шансы на успех. 
Шура мнение... – отвечает 'да' или 'нет'.
Шип – соединяет двух участников чата. 💘
Зов гоев – отмечает всех участников чата. 🐑 """)
    
msg_text = MsgText()