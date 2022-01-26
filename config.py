from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8806700"))
API_HASH = getenv("API_HASH", "e3be731079b3d459bac857e7eec3ee87)
BOT_TOKEN = getenv("BOT_TOKEN","5109963129:AAEh1nsreej43O1jyr57ZBP13aKaf3z_7A0")
BOT_NAME = getenv("BOT_NAME","👑⃝⃟𝐁𝐇ͫA̶T̶A̶K̶𝐓𝐈⃟🦞━▣𓆩👅𓆪▣━👻⃝🇦𝐓𝐌𝐀⃝🖤✿❯━━━━𓆩👅𓆪𒆜𓊈⋆⃟𝘿𝙍𝘼𝙂𝙊𝙉𝙕⋆⃟𓊉 ✘『🇮🇳』➤🖤🚩")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQCdZUPVqWdHudEeVSwMaYj2FoNB7x5LMGmFBTSe603Zo8shg0e_pxyqAJ59lxCvBblBOg-yn3nxNkzleIuv3q4poErGNQLNy2QL11BBjiZv2FK47xWn522ECLgWUg4Tnxhs_gkOZQjWkLkP1NWibeaxy0y5ufTaDS905u7ksMedBw_XBjeZHFkL4kLdRbnerhijU2UP1aJ0QfEN9nrSSDJj6NxxrFpg53nnlT4H9MXyZkGvMa9_CERrgCVlyz4bKcEOqw9RrQk6PhwnawfbkP3ESgFLT3FtBCvmZGFDTY2-1wFQzla9mK00KluI2n_266KZJqFnHLXIbR329-Yyy2ddbAMQnwA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5080000553").split()))
