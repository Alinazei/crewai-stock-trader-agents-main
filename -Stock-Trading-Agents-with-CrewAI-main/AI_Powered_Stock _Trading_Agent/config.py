import os

# NVIDIA API Configuration
# Set these environment variables before running the application
os.environ['USE_NVIDIA_API'] = 'true'
os.environ['NVIDIA_API_BASE_URL'] = 'https://integrate.api.nvidia.com/v1'
os.environ['NVIDIA_API_KEY'] = ''
os.environ['NVIDIA_MODEL'] = 'meta/llama-3.1-405b-instruct'
os.environ['NVIDIA_TEMPERATURE'] = '0.3'
os.environ['NVIDIA_TOP_P'] = '0.7'
os.environ['NVIDIA_MAX_TOKENS'] = '8192'

# Alternative models you can use:
# os.environ['NVIDIA_MODEL'] = 'meta/llama-3.3-70b-instruct'
# os.environ['NVIDIA_MODEL'] = 'qwen/qwen3-235b-a22b'

# Twitter API Configuration
# Twitter API - Apply for access at https://developer.twitter.com
os.environ['TWITTER_BEARER_TOKEN'] = ''
os.environ['TWITTER_API_KEY'] = ''
os.environ['TWITTER_API_SECRET'] = ''
os.environ['TWITTER_ACCESS_TOKEN'] = ''
os.environ['TWITTER_ACCESS_TOKEN_SECRET'] = ''

# Default watchlist for trading
DEFAULT_WATCHLIST = "NIO,SNDL,IGC,TLRY,UGRO,CGC,EGO,OGI" 
