import asyncio
import lichessbotpoetry.api as api
import lichessbotpoetry.server as server
import os
#import threading
import multiprocessing

task = None

async def stream():    
  global task
  task = asyncio.create_task(api.stream("api/stream/event", os.getenv("RUSTBOT_TOKEN")))
  print("task", task)
  await task
  print("task done")

async def main():      
    await asyncio.gather(stream())

while True:    
  try:
    #t = threading.Thread(target=server.run_server)
    #t.start()
    p = multiprocessing.Process(target=server.run_server)
    p.start()
    print("server started")
    asyncio.run(main())
    #main()
  except KeyboardInterrupt:
    if not task is None:
      print("cancelling task")
      task.cancel()
    else:
      print("no task to cancel")
  stop = input("stop?")
  if ( stop == "y" ) or ( stop == "Y" ):
    break
