import asyncio, asyncvnc
from PIL import Image

async def run_client():
    async with asyncvnc.connect('10.151.116.100', 5901) as client:
        client.mouse.move(300, 315)
        client.mouse.click()
        
        client.keyboard.write('hello world!')
        print(client.video.width, client.video.height)
        pixels = await client.screenshot()

        # Save as PNG using PIL/pillow
        image = Image.fromarray(pixels)
        image.save('screenshot.png')

asyncio.run(run_client())
