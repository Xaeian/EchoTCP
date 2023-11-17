import asyncio

IP = "127.0.0.1"
PORT = 7357
BUFF = 2**14
SEND = ["Hello", b"Hi\x99"]

async def conn(request:bytes|str):
  if type(request) is str:
    request = bytes(request, "utf-8")
  reader, writer = await asyncio.open_connection(IP, PORT)
  writer.write(request)
  await writer.drain()
  response = await reader.read(BUFF)
  print(response)
  writer.close()
  await writer.wait_closed()

if type(SEND) in (list, tuple):
  async def main():
    tasks = [conn(req) for req in SEND]
    await asyncio.gather(*tasks)
  asyncio.run(main())
else:
  asyncio.run(conn(SEND))
