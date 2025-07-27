import os

# NVIDIA API Configuration
# Set these environment variables before running the application
os.environ['USE_NVIDIA_API'] = 'true'
os.environ['NVIDIA_API_BASE_URL'] = 'https://integrate.api.nvidia.com/v1'
os.environ['NVIDIA_API_KEY'] = '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'
os.environ['NVIDIA_MODEL'] = 'meta/llama-3.1-405b-instruct'
os.environ['NVIDIA_TEMPERATURE'] = '0.3'
os.environ['NVIDIA_TOP_P'] = '0.7'
os.environ['NVIDIA_MAX_TOKENS'] = '8192'

# Alternative models you can use:
# os.environ['NVIDIA_MODEL'] = 'meta/llama-3.3-70b-instruct'
# os.environ['NVIDIA_MODEL'] = 'qwen/qwen3-235b-a22b'

# Twitter API Configuration
# Twitter API - Apply for access at https://developer.twitter.com
os.environ['TWITTER_BEARER_TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAOUz3AEAAAAAVW6bvkdkd2bLraakw2qI0yycsGw%3D4WUeXscApWAaEctlQKIskECdPsB1YLmnncSdqJXvDgcGHGI6vx'
os.environ['TWITTER_API_KEY'] = 'nlNW0U0AO74FgCBLrRxBcrLka'
os.environ['TWITTER_API_SECRET'] = 'LvjSeUVBTwFo1kF8zfw5poUcg6E7JPsu73OrXfom28UioNPR3u'
os.environ['TWITTER_ACCESS_TOKEN'] = '1944533922315984897-xu9TnhRh9NoMSDBoirpeYENYII0Clr'
os.environ['TWITTER_ACCESS_TOKEN_SECRET'] = 'qOdnUosojw9BTpMZSshkLIHiTxY2OD0QvkQ74XiA06GpO'

# Default watchlist for trading
DEFAULT_WATCHLIST = "NIO,SNDL,IGC,TLRY,UGRO,CGC,EGO,OGI" 