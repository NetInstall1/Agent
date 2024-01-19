import asyncio
import socketio
import json

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print(f'Connection Established \nsocketId {sio.get_sid()}')
    socket_id = sio.get_sid()
    agent_id = await getAgentId()
    data = {
        "agent_id": agent_id,
        "socket_id": socket_id
    }
    await sio.emit('agent-connect', data)

@sio.on('room-joined')
async def room_joined(data):
    print(data)
    print('Room joined!')


async def getAgentId():
    with open('config.json') as f:
        config = json.load(f)
        agent_id = config.get('agent_id')
    
    return agent_id

async def main():
    with open('config.json') as f:
        config = json.load(f)
        server_url = config.get('server_url')
        print(server_url)
    await sio.connect(server_url)
    await sio.wait()

    
if __name__ == '__main__':

    asyncio.run(main())