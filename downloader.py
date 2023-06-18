import asyncio
import argparse

from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import ConnectEvent

parser = argparse.ArgumentParser(description='Tik tok live stream downloader')

parser.add_argument('--timeOut', type=int,
                    help='time out time - optional')

parser.add_argument('userName', 
                    help='user name to download')

parser.add_argument('--output',  required=True,
                    help='output path')

args = parser.parse_args()

userName = args.userName

client = TikTokLiveClient(userName)


@client.on("connect")
async def on_connect(_: ConnectEvent):

    client.download(
        path=args.output, 
        duration=None,
        quality="ld" 
    )

    await asyncio.sleep(2)
    client.stop_download()


if __name__ == '__main__':

    client.run()