from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import random

# حط التوكن مالتك هنا بين ""
TOKEN = "8111923797:AAEgmNQqwsXwvdkIOhY3sdYtG11UZPR0z6k"

choices = ['حجر', 'ورقة', 'مقص']

# ------------------- /start -------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name

    keyboard = [
        [InlineKeyboardButton("🪨 حجرة ورقة مقص", callback_data='play')],
        [InlineKeyboardButton("🔢 تخمين الرقم", callback_data='guess')],
        [InlineKeyboardButton("🪙 رمي العملة", callback_data='coin')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"أهلاً {user}، مرحباً بك في بوت الألعاب!\n"
        "اختر لعبة من القائمة:",
        reply_markup=reply_markup
    )

# ------------------- زر الضغط -------------------
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'play':
        await query.message.reply_text("🪨✂️📄 لعبة حجرة ورقة مقص:\nارسل:\n/play حجر أو /play ورقة أو /play مقص")
    elif query.data == 'guess':
        await query.message.reply_text("🔢 لعبة تخمين الرقم:\nارسل رقم بين 1 إلى 10 مثل:\n/guess 7")
    elif query.data == 'coin':
        result = random.choice(["وجه", "كتابة"])
        await query.message.reply_text(f"🪙 تم رمي العملة: {result}")

# ------------------- /play -------------------
def determine_winner(player, bot):
    if player == bot:
        return "تعادل!"
    elif (player == 'حجر' and bot == 'مقص') or \
         (player == 'ورقة' and bot == 'حجر') or \
         (player == 'مقص' and bot == 'ورقة'):
        return "أنت الفائز!"
    else:
        return "البوت فاز!"

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("🪨✂️📄 لعبة حجرة ورقة مقص:\nارسل:\n/play حجر\n/play ورقة\n/play مقص")
        return

    player_choice = context.args[0]
    if player_choice not in choices:
        await update.message.reply_text("❌ الرجاء اختيار: حجر، ورقة أو مقص فقط.")
        return

    bot_choice = random.choice(choices)
    result = determine_winner(player_choice, bot_choice)

    await update.message.reply_text(
        f"أنت اخترت: {player_choice}\n"
        f"البوت اختار: {bot_choice}\n\n"
        f"{result}"
    )

# ------------------- /guess -------------------
async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("🔢 لعبة تخمين الرقم:\nارسل رقم بين 1 إلى 10 مثل:\n/guess 7")
        return

    try:
        user_guess = int(context.args[0])
        if not 1 <= user_guess <= 10:
            raise ValueError
    except ValueError:
        await update.message.reply_text("❌ اكتب رقم صحيح بين 1 و 10.")
        return

    actual_number = random.randint(1, 10)
    if user_guess == actual_number:
        await update.message.reply_text(f"🎉 صحيح! الرقم هو {actual_number} ✅")
    else:
        await update.message.reply_text(f"😢 غلط! الرقم الصحيح كان {actual_number} ❌")

# ------------------- /coin -------------------
async def coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = random.choice(["وجه", "كتابة"])
    await update.message.reply_text(f"🪙 النتيجة: {result}")

# ------------------- تشغيل البوت -------------------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("play", play))
app.add_handler(CommandHandler("guess", guess))
app.add_handler(CommandHandler("coin", coin))
app.add_handler(CallbackQueryHandler(handle_buttons))

app.run_polling()
# هذا هو بوت تلغرام بسيط للألعاب
# يحتوي على ألعاب مثل حجرة ورقة مقص، تخمين الرقم، ورمي العملة
# يمكنك إضافة المزيد من الألعاب أو تحسين الكود حسب الحاجة
# تأكد من تثبيت مكتبة python-telegram-bot
# باستخدام الأمر:
# pip install python-telegram-bot --upgrade
# ثم قم بتشغيل البوت باستخدام:
# python tel_bot.py
# تأكد من وضع التوكن الخاص بك في المكان المناسب
# قبل تشغيل البوت
# يمكنك استخدام هذا البوت في أي مجموعة أو دردشة خاصة
# مع الأصدقاء
# استمتع بالألعاب!
# يمكنك إضافة المزيد من الميزات أو الألعاب حسب رغبتك
# تأكد من أن لديك توكن بوت تلغرام صالح
# يمكنك الحصول على توكن من خلال إنشاء بوت جديد باستخدام
# BotFather على تلغرام
