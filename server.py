import asyncio, requests, os, time
from log import logger

time.sleep(3)

PATH = os.path.dirname(os.path.abspath(__file__))
if os.name == "posix": IP = os.popen('curl -s ifconfig.me').readline()
else: IP = requests.get("https://ifconfig.me/ip").text.strip()
# IP = "127.0.0.1"
PORT = 7357
BUFF = 2**14

log = logger(f"{PATH}/echotcp.log")

async def loop(reader:asyncio.StreamReader, writer:asyncio.StreamWriter):
  request = await reader.read(BUFF)
  ip, port = writer.get_extra_info('peername')
  response = f"IP:{ip} Port:{port} Size:{len(request)} Data:"
  log.info(response + str(request))
  writer.write(bytes(response, "utf-8") + request)
  await writer.drain()
  writer.close()

async def main():
  server = await asyncio.start_server(loop, IP, PORT) # create tcp/ip server
  async with server: # working with async model
    await server.serve_forever()

log.info(f"Echo TCP/IP application {IP}:{PORT} has been running")
asyncio.run(main())
