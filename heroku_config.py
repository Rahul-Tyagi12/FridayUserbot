import os


class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 1310683))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "b735d306fc6ee8773aedf5022224bcea")
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOLQBu1-lKtR3NFTrFGzW43wraIkEBRJIuuk5QDr7TiF0ItxLU4fxb0zrOqqPL2f57mVIvUKdXpOGcO-GaU-z1hqxk2eXG48_MCDzXJVOMtkTWJjxDT8SBc2INRHpGSfvVCpKT0J6qljdsAI59KZfx5hqmhuDvy2iCdbnOx5_iyUsTHnzaFHMUpCrvedJayTTaTEp7hhEoC3VlPdOtXxZljOX7x8xk6ftNncnZRgcurpj3naRHkDZPactbt7mXfyORO3BkUBz768b59Uwl-KPNibWDqiN_3jnnSPl7dKENpgknRA-1aeEFWQlTEcslg18YHacVKXdQE8xEUwPjtNzZXQuw2M=)
    DB_URI = os.environ.get("DATABASE_URL", "postgres://qfqezgkyzmaroa:9da51846247fa5f397ffa75305b270903db2e548fbb46b2b9b8afbad14f38448@ec2-54-224-124-241.compute-1.amazonaws.com:5432/dcsus5shiqp5p3")
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", None)
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", "d98aac5deb2d723265d0dfb3a313d9357269afaa")
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", "Rahul-Tyagi12/FridayUserbot")
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "35403cd6-12ce-471e-a1ca-419bd1a6fcd7")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "fridayb")
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", "1166953761:AAFudTLG9VcLJEsrnc3rrEZ1N-6Vpk23qeE")
    # Send .get_id in any channel to fill this value.
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", -1001224333565))
    PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID", -1001224333565))
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", "@Tonysfridaybot")
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    if AUTH_TOKEN_DATA is not None:
        if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
            os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID", -1001224333565))
    NEWS_CHANNEL_ID = int(os.environ.get("NEWS_CHANNEL_ID", -100))
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    ANTISPAM_SYSTEM = os.environ.get("ANTISPAM_SYSTEM", "DISABLE")
    WHITE_CHAT = set(int(x) for x in os.environ.get("WHITE_CHAT", "").split())


class Development(Var):
    LOGGER = True
