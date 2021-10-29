class script(object):
    START_TXT = """Merhaba {},
Benim Adım <a href='https://t.me/QuickwasteBot'>Quickwaste Film Botu</a>, Film Sağlayabilirim, sadece beni grubuna ekle ve keyfini Çıkar. 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
İşte Komutlarım İçin Yardım ."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: Quickwaste Film Botu
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: ali
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://github.com/EvamariaTG/EvaMaria  

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>Sohbet için bir filtre ekle</code>
• /filters - <code>Tüm Filtrelerin listesi</code>
• /del - <code>sohbette belirli bir filtreyi silme</code>
• /delall - <code>sohbetteki tüm filtreleri silme (Sohbet Kurucusu Sadece)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Quickwaste Film Botu Hem URL hem de uyarı satır içi düğmelerini destekler .

<b>NOTE:</b>
1. Telegram herhangi bir içerik olmadan düğme göndermenize izin vermez, bu nedenle içerik zorunludur.
2. Eva Maria, herhangi bir telegram medya türüne sahip düğmeleri destekler.
3. Düğmeler markdown biçimi olarak düzgün bir şekilde ayrıştırılmalıdır

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Özelse beni kanalınızın yöneticisi yap.
2. Kanalınızın kam rip, porno ve sahte dosyalar içermediğinden emin olun.
3. Son mesajı bana alıntılarla iletin.
 O kanaldaki tüm dosyaları veritabanıma ekleyeceğim. ."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Filtreleri yönetmek için botu PM'ye bağlamak için kullanılır 
- gruplar halinde spam'leri önlemeye yardımcı olur. 

<b>NOTE:</b>
1. Yalnızca yöneticiler bağlantı ekleyebilir .
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of tessa

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all tssa users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
