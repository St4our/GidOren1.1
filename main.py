from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.button import Button


from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout


from kivymd.uix.button import MDFloatingActionButton




KV = '''
<ContentNavigationDrawer>

    MDList:

        OneLineListItem:
            text: "Главная"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 1"


        OneLineListItem:
            text: "Парки"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"

        OneLineListItem:
            text: "Сады"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 3"
        OneLineListItem:
            text: "Кинотеатры"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 4"


        OneLineListItem:
            text: "Карта"
            on_press:
                import webbrowser
                webbrowser.open("https://yandex.ru/maps/?from=tabbar&ll=55.307388%2C51.795769&mode=search&sctx=ZAAAAAgCEAAaKAoSCSF00CUcmEtAEbQiaqLP7UlAEhIJpyA%2FG7lu1T8Rrir7rgj%2Buz8iBgABAgMEBSgKOABAjooGSAFiIW1pZGRsZV9wb3N0ZmlsdGVyX3RocmVzaGNoYWluPTAuNGIhYWRkX3NuaXBwZXQ9dG9wb255bV9kaXNjb3ZlcnkvMS54YhxtaWRkbGVfcG9zdGZpbHRlcl90aHJlc2g9MC40YipyZWxldl9yYW5raW5nX21zZV9mb3JtdWxhPW1zZV9kYzExMTc2Ml9leHBiNnJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vQ29sbGVjdGlvbnMvUmFuZG9tUG9zaXRpb249dHJ1ZWJCcmVhcnI9c2NoZW1lX0xvY2FsL0dlby9MaXN0RGlzY292ZXJ5L0VuYWJsZURpc2NvdmVyeVRleHRSZXF1ZXN0cz0xYjpyZWFycj1zY2hlbWVfTG9jYWwvR2VvL0xpc3REaXNjb3ZlcnkvRW5hYmxlRW1wdHlSZXF1ZXN0cz0xYjpyZWFycj1zY2hlbWVfTG9jYWwvR2VvL0xpc3REaXNjb3ZlcnkvRW5hYmxlQ29tbW9uUGljTWVudT0xYjVyZWFycj1zY2hlbWVfTG9jYWwvR2VvL0xpc3REaXNjb3ZlcnkvRW5hYmxlUmVxdWVzdHM9MWIwcmVhcnI9c2NoZW1lX0xvY2FsL0dlby9Bc2tEaXNjb3ZlcnlGb3JUb3Bvbnltcz0xYjJyZWFycj1zY2hlbWVfTG9jYWwvR2VvL0NvbGxlY3Rpb25zL0VuYWJsZWRNaXg9dHJ1ZWI1cmVhcnI9c2NoZW1lX0xvY2FsL0dlby9MaXN0RGlzY292ZXJ5L0VuYWJsZVZlcnRpY2FsPTFiUHJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vQnVzR2VvQ2hvb3NlL1Rha2VSdWJyaWNGaXJzdFNhbWVCeVJlc3VsdHNNc2VUaHJlc2hvbGQ9MC40agJydZ0BzcxMPaABAKgBAL0BXEUVPcIBWqrJmfcE77D2xKAEoc%2Fz%2F%2FYBivPWkK0DyoTKtaMCnfCtnQX3r8WbzAKLq5zsA%2BGctfRw8d%2Fi2%2FIB%2F6n0yI8Bi%2Bi4mga6xsLc2QHMq5u5BobShNWeA5y4t8bbBOoBAPIBAPgBAIICJNC60YPQtNCwINC%2F0L7QudGC0Lgg0L7RgNC10L3QsdGD0YDQs4oCxgMxODQxMDYzNDYkMTg0MTA2MzcwJDE4NDEwNjM1NCQxODQxMDYzODAkODg4NDQ1NzU2OTMkMTg0MTA2MzcyJDMxMzcwMTYzNjAzJDI1NjAzNzM2MiQxODQxMDYzNTAkMTg0MTA2MzQ0JDE5MjQ0ODA5MjgzJDU2Mzk2NzEwODk1JDE4NDEwNjM2OCQxOTc5NDY0MzUwMTEkMTg0MTA1ODk0JDE4NDEwNTg3MiQxODQxMDYzNDAkMTg0MTA2MzQyJDE4NDEwNjM5MCQxODQxMDYzNjAkMTg0MTA2Mzc4JDE4NDEwNjM5NCQxODQxMDU5MTgkMTg0MTA1ODY4JDM1MzI1MTQwMjM4JDE4NDEwNTg3NiQxODQxMDU5MDIkMTg0MTA1ODgwJDE4NDEwNzI3NSQxODQxMDYzNTgkMTg0MTA2MzkyJDIxNTA2NzIwNjI3NyQxODQxMDU4OTIkMTg0MTA2MzU2JDE4NDEwNjMzMiQxMzg3Nzg4OTk2JDE4NDEwNjMzNCQzNTE5MzExNDkzNyQ3ODA5MjgzMzgkMTg0MTA1OTAwJDE4NDEwNTgzOCQxOTE0NzI2ODk2NzIkMTk5MTU4Nzk3NzgykgICNDiaAgxkZXNrdG9wLW1hcHM%3D&sll=55.307388%2C51.795769&source=serp_navig&sspn=0.689392%2C0.258012&text=куда%20пойти%20оренбург&z=11")
                


        OneLineListItem:
            text: "Выход"
            padding: 90, 56, 12, 16
            on_press:
                app.stop()
                
                


MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        elevation: 4
        title: "ОренбургГид"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        
    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                MDLabel:
                    text: "Главная страница ОренбургГид"
                    halign: "center"

            MDScreen:
                name: "scr 2"

                MDTabs:
                    id: tabs
                    
                    
                    Tab:
                        id: tab1
                        title: "Тополя"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"

                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-sad-topolya-1-1024x698.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Парк «Тополя»"
                                    bold: True
                                    color: "white"
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/topolya/221940216026/?ll=55.091853%2C51.769275&z=16.45")
                                        
                            MDLabel:
                                text: "Этот парк считается лучшим местом для семейного отдыха в городе. В теплое время года на территории парка работает множество аттракционов и тематических зон."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"                                    


                    Tab:
                        id: tab2
                        title: "Гуськова"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-park-guskova-3-1024x715.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Парк им. Л.А. Гуськова"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/park_imeni_l_a_guskova/191430380802/?ll=55.142669%2C51.805034&z=16.09")
                                        
                            MDLabel:
                                text: "В центре парка расположен Памятник доблестным советским воинам. На аллеях, прилегающих к главной площади, установлены памятники «Детям войны», «Звезда», «Серп и молот»."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"

                    Tab:
                        id: tab3
                        title: "им. 50-летия СССР"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-park-50-letiya-sssr-3-1024x683.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Парк им. 50-летия СССР"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/park_kultury_i_otdykha_50_let_sssr/166782001728/?ll=55.135246%2C51.832152&z=16.27")
                                        
                            MDLabel:
                                text: "В теплое время года в парке работают аттракционы, батуты и тир. На территории есть несколько кафе, в которых можно выпить кофе и подкрепится. Замечательное место для отдыха всей семьей."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"
                    Tab:
                        id: tab4
                        title: "им. Перовского"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-park-perovskogo-4-1024x768.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Парк им. Перовского"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/park_imeni_v_a_perovskogo/164308038518/?ll=55.093642%2C51.771327&z=16.74")
                                        
                            MDLabel:
                                text: "Парк имеет обширную инфраструктуру. В парке обустроена специальная площадка с тренажерами, футбольное мини-поле, зоны для игры в баскетбол и настольный теннис, а также трамплин для катания на велосипеде и скейтборде."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"

                                
                                
                    Tab:
                        id: tab5
                        title: "Набережная Оренбурга"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-pushkinskij-bulvar-na-naberezhnoj-3-1024x620.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Набережная Оренбурга"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/orenburgskaya_naberezhnaya/7292358936/?ll=55.192684%2C51.777188&z=11.38")
                                        
                            MDLabel:
                                text: "Инфраструктура парка очень насыщенная. В центре бульвара расположена лестница, ведущая к пешеходному посту через Урал. Вдоль неё есть лавочки и беседки для отдыха. Установлено освещение."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"

                                
                    Tab:
                        id: tab6
                        title: "Зауральная роща"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-zauralnaya-roshcha-2-1024x768.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Зауральная роща"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/zauralnaya_roshcha/25668124635/?ll=55.115173%2C51.747305&z=14.94")
                                        
                            MDLabel:
                                text: "После реконструкции Зауральная роща обзавелась детским автодромом и новой спортивной площадкой. В летнее время в парке работает тир и детские аттракционы. Этот парк относят к числу самых посещаемых мест в городе."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"
                        
                    Tab:
                        id: tab7
                        title: "50-летия ВЛКСМ"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "park-50-let-vlksm-2.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Парк 50-летия ВЛКСМ"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/park_kultury_i_otdykha_50_let_sssr/166782001728/?ll=55.135246%2C51.832152&z=16.27")
                                        
                            MDLabel:
                                text: "На территории самого парка никаких строений нет. Рядом располагается Центр настольного тенниса России."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"
                                
                                    


            MDScreen:
                name: "scr 3"

                MDTabs:
                    id: tabs
                                      
                    Tab:
                        id: tab8
                        title: "Октябрьской Революции"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-sad-oktyabrskoj-revolyucii-1-1024x657.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Сад Октябрьской Революции"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/sad_imeni_oktyabrskoy_revolyutsii/23333542339/?ll=55.099190%2C51.790026&z=17.94")
                                        
                            MDLabel:
                                text: "Треть всей площади сада была отдана под строительство спортивного комплекса. Также на исторической территории парка расположен кинотеатр, детский сад и недостроенный дом культуры."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"

                    Tab:
                        id: tab9
                        title: "Фрунзе"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-sad-frunze-3-1024x687.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Сад Фрунзе"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/48/orenburg/geo/sad_imeni_frunze/120718880/?ll=55.091054%2C51.760390&z=17.54")
                                        
                            MDLabel:
                                text: "На территории парка открыт музей под открытым небом, посвященный советским солдатам. Установлена часовня."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"

                    Tab:
                        id: tab10
                        title: "Цвиллинга"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "orenburg-sad-cvillinga-5-1024x768.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Сад Цвиллинга"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/park_im_tsvillinga/19923912117/?ll=55.068343%2C51.785229&z=17.54")
                                        
                            MDLabel:
                                text: "Сад оснащен всей необходимой инфраструктурой. Есть лавочки для отдыха, зоны для игры в футбол и настольный теннис. В зимнее время в парке заливают каток."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"                
                    

                    


            MDScreen:
                name: "scr 4"

                MDTabs:
                    id: tabs
                                      
                    Tab:
                        id: tab11
                        title: "Кинодом"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "kinodom.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Кинодом"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/kinodom/222967841250/?indoorLevel=1&ll=55.181478%2C51.812682&z=16.53")
                                        
                            MDLabel:
                                text: "Уникальная особенность кинотеатра - специально разработанные премиальные мягкие кресла и 2-х местные диваны вместо стандартных кинотеатральных кресел."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"

                    Tab:
                        id: tab12
                        title: "Космос"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "XXL.jpg"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Космос"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/kosmos/243619535364/?ll=55.092338%2C51.770478&z=16.53")
                                        
                            MDLabel:
                                text: "Основная особенность заключается в том, что достроенный кинотеатр находится под землей. В старом здании также прошла реконструкция, в нем установили современное оборудование, создали новую архитектуру и интерьер."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"

                    Tab:
                        id: tab13
                        title: "Мармелад Синема"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "marmelad.JPG"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Мармелад Синема"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/marmelad_sinema/189499497619/?indoorLevel=1&ll=55.117706%2C51.843896&z=16.53")
                                        
                            MDLabel:
                                text: "Для вашего удобства предусмотрены 9 комфортных залов с удобными креслами и отличным звуком."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"

                    Tab:
                        id: tab14
                        title: "Мистер Фёст"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "first.JPG"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Мистер Фест"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/mister_fyost/71450799782/?indoorLevel=1&ll=55.198411%2C51.775851&z=16.93")
                                        
                            MDLabel:
                                text: "Киноцентр Мистер Фёст это: 5 залов на 600 мест, concession-бар с сотней видов попкорна, начос, соусов и напитков, продвинутая репертуарная политика - максимум премьер, а также три вида кресел, в том числе места для поцелуев ;)."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"

                    Tab:
                        id: tab15
                        title: "Синема 5 Гуливер"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "guliver.JPG"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Синема 5 Гуливер"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/sinema_5/1159699073/?display-text=%D1%81%D0%B8%D0%BD%D0%B5%D0%BC%D0%B0%205%20%D0%B3%D1%83%D0%BB%D0%BB%D0%B8%D0%B2%D0%B5%D1%80&indoorLevel=1&ll=55.091026%2C51.811394&mode=search&sctx=ZAAAAAgBEAAaKAoSCVUVGohlmUtAEdLI5xVP40lAEhIJg4jUtItplj8R%2BKdUibK3hD8iBgABAgMEBSgKOABA258NSAFiIWFkZF9zbmlwcGV0PXRvcG9ueW1fZGlzY292ZXJ5LzEueGI2cmVhcnI9c2NoZW1lX0xvY2FsL0dlby9Db2xsZWN0aW9ucy9SYW5kb21Qb3NpdGlvbj10cnVlYkJyZWFycj1zY2hlbWVfTG9jYWwvR2VvL0xpc3REaXNjb3ZlcnkvRW5hYmxlRGlzY292ZXJ5VGV4dFJlcXVlc3RzPTFiOnJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vTGlzdERpc2NvdmVyeS9FbmFibGVFbXB0eVJlcXVlc3RzPTFiOnJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vTGlzdERpc2NvdmVyeS9FbmFibGVDb21tb25QaWNNZW51PTFiNXJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vTGlzdERpc2NvdmVyeS9FbmFibGVSZXF1ZXN0cz0xYjByZWFycj1zY2hlbWVfTG9jYWwvR2VvL0Fza0Rpc2NvdmVyeUZvclRvcG9ueW1zPTFiMnJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vQ29sbGVjdGlvbnMvRW5hYmxlZE1peD10cnVlYjVyZWFycj1zY2hlbWVfTG9jYWwvR2VvL0xpc3REaXNjb3ZlcnkvRW5hYmxlVmVydGljYWw9MWoCcnWdAc3MTD2gAQCoAQC9AWnxD3HCAQWBtf6oBOoBAPIBAPgBAIICH9GB0LjQvdC10LzQsCA1INCz0YPQu9C70LjQstC10YCKAgCSAgCaAgxkZXNrdG9wLW1hcHM%3D&sll=55.091026%2C51.811394&sspn=0.016743%2C0.005493&text=%D1%81%D0%B8%D0%BD%D0%B5%D0%BC%D0%B0%205%20%D0%B3%D1%83%D0%BB%D0%BB%D0%B8%D0%B2%D0%B5%D1%80&z=16.88")
                                        
                            MDLabel:
                                text: "Обновленное оборудование позволяет  зрителям оценить уникальные возможности 3D и получить удовольствие от просмотра каждого фильма. Залы оснащены эргономичными креслами в обычных залах и мягкими двухместными диванами со столиками  в зале «Комфорт». Дополнением к уютной атмосфере «Синема 5» служит кафе-бар, где можно приобрести различные закуски и напитки. Репертуарная политика включает в себя крупные релизы и блокбастеры, а также фильмы ограниченного проката для настоящих гурманов."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"
                    Tab:
                        id: tab16
                        title: "Синема 5 Север"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "sever.JPG"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Синема 5 Север"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/sinema_5/1228265818/?indoorLevel=1&ll=55.127711%2C51.833072&mode=search&sctx=ZAAAAAgBEAAaKAoSCRNGs7J9kEtAEd1ELc2t6klAEhIJxqUqbXGNnz8RD167tOGwhD8iBgABAgMEBSgKOABA2p8NSAFiIWFkZF9zbmlwcGV0PXRvcG9ueW1fZGlzY292ZXJ5LzEueGI2cmVhcnI9c2NoZW1lX0xvY2FsL0dlby9Db2xsZWN0aW9ucy9SYW5kb21Qb3NpdGlvbj10cnVlYkJyZWFycj1zY2hlbWVfTG9jYWwvR2VvL0xpc3REaXNjb3ZlcnkvRW5hYmxlRGlzY292ZXJ5VGV4dFJlcXVlc3RzPTFiOnJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vTGlzdERpc2NvdmVyeS9FbmFibGVFbXB0eVJlcXVlc3RzPTFiOnJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vTGlzdERpc2NvdmVyeS9FbmFibGVDb21tb25QaWNNZW51PTFiNXJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vTGlzdERpc2NvdmVyeS9FbmFibGVSZXF1ZXN0cz0xYjByZWFycj1zY2hlbWVfTG9jYWwvR2VvL0Fza0Rpc2NvdmVyeUZvclRvcG9ueW1zPTFiMnJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vQ29sbGVjdGlvbnMvRW5hYmxlZE1peD10cnVlYjVyZWFycj1zY2hlbWVfTG9jYWwvR2VvL0xpc3REaXNjb3ZlcnkvRW5hYmxlVmVydGljYWw9MWoCcnWdAc3MTD2gAQCoAQC9AXUCbcvCAQXastfJBOoBAPIBAPgBAIICGdGB0LjQvdC10LzQsCA1INGB0LXQstC10YCKAgCSAgCaAgxkZXNrdG9wLW1hcHM%3D&sll=55.127711%2C51.833072&sspn=0.018322%2C0.006008&text=%D1%81%D0%B8%D0%BD%D0%B5%D0%BC%D0%B0%205%20%D1%81%D0%B5%D0%B2%D0%B5%D1%80&z=16.75")
                                        
                            MDLabel:
                                text: "Вмещает в себя семь зрительных залов. Все они оснащены современным техническим оборудованием и цифровой системой, позволяющей просматривать кинофильмы в 3D формате. Во всех залах есть мягкие удобные сидения, лестничная подсветка и система кондиционирования зима-лето. Каждый посетитель имеет возможность просмотреть мировые премьеры фильмов и насладиться полным комфортом."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"

                    Tab:
                        id: tab17
                        title: "Сокол"
                        
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "22dp"
                                

                            MDSmartTile:
                                
                                radius: 24
                                box_radius: [0, 0, 24, 24]
                                box_color: 0, 0, 0, .7
                                source: "sokol.JPG"
                                
                                size_hint: None, None
                                size: "320dp", "320dp"
                                
                                
                                

                                MDIconButton:
                                    icon: "heart-outline"
                                    theme_icon_color: "Custom"
                                    icon_color: 1, 0, 0, 1
                                    pos_hint: {"center_y": .5}
                                    on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                MDLabel:
                                    text: "Сокол"
                                    bold: True
                                    color: 1, 1, 1, 1
                                MDRectangleFlatButton:
                                    text: "На карте"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    on_press:
                                        import webbrowser
                                        webbrowser.open("https://yandex.ru/maps/org/sokol/1104302040/?indoorLevel=1&ll=55.129931%2C51.794381&mode=search&sll=55.129931%2C51.795346&sspn=0.006086%2C0.001997&text=%D0%A1%D0%BE%D0%BA%D0%BE%D0%BB&z=16.77")
                                        
                            MDLabel:
                                text: "Система звука Dolby и огромный широкоформатный экран, дает зрителю возможность полчувствовать себя участником происходящего на экране. Реалистичность показа, вот что привлекает современного зрителя. Большой зал вмещает в себя – 283 посадочных места."
                                bold: True
                                color: 1, 1, 1, 1
                                halign: "left"
            MDScreen:
                name: "scr 5"

                MDLabel:
                    text: "Карта"
                    halign: "center"
                    
                MDScreen:
                    name: "scr 6"

                MDLabel:
                    text: "Выход"
                    halign: "center"


                
                
                    

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
                


'''



    
class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Tab(MDFloatLayout, MDTabsBase):
    pass


class GidOren(MDApp):
    title = "GidOren"

    
    
    def build(self):

        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)
    


    
        

GidOren().run()
