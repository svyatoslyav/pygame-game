import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("audio.mp3")
pygame.mixer.music.set_volume(0.4)
hitsound = pygame.mixer.Sound("sound-hit.wav")
hitsound.set_volume(0.06)
musicplaying = False

#screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("osu parody")
screen.fill("white")

#timers
clock = pygame.time.Clock()
timer = 0
FPS=120

#stats
pressrating = 0
rating = 0
notespeed = 800 # px/sec
marv_count =0
perf_count =0
great_count =0
good_count =0
okay_count =0
miss_count =0

#objects
ratetext = ""
baseline = pygame.Rect(0, HEIGHT-50, WIDTH, 5)
notes_row1 =  [13.039, 13.839, 14.439, 15.239, 16.039, 16.639, 17.239, 17.639, 18.439, 19.439, 20.039, 20.839, 21.839, 22.439, 23.239, 24.239, 25.239, 25.639, 26.039, 26.439, 27.039, 27.439, 28.039, 28.639, 29.239, 29.839, 30.239, 30.839, 31.439, 32.039, 32.439, 33.239, 33.639, 34.439, 34.839, 35.239, 35.639, 36.139, 36.439, 36.839, 38.439, 38.739, 38.939, 39.239, 39.439, 39.639, 39.939, 40.339, 40.739, 41.039, 41.239, 41.439, 41.739, 42.039, 42.239, 42.439, 42.739, 43.039, 43.239, 43.639, 44.039, 44.239, 44.639, 44.839, 45.139, 45.439, 45.839, 46.139, 46.439, 46.839, 47.039, 47.239, 47.539, 47.839, 48.039, 48.339, 48.639, 49.039, 49.239, 49.539, 49.839, 50.039, 50.439, 50.839, 51.239, 51.639, 51.839, 52.339, 52.639, 52.839, 53.239, 53.439, 53.739, 53.939, 54.139, 54.339, 54.639, 54.939, 55.339, 55.639, 55.839, 56.139, 56.439, 56.639, 56.839, 57.239, 57.439, 57.639, 58.039, 58.339, 58.839, 59.039, 59.339, 59.739, 60.039, 60.439, 60.639, 60.939, 61.239, 61.439, 61.739, 62.039, 62.239, 62.439, 62.839, 63.039, 63.239, 63.639, 64.039, 64.439, 64.839, 65.439, 65.839, 66.439, 67.039, 67.639, 68.239, 68.639, 69.239, 69.839, 70.439, 70.839, 71.639, 72.039, 72.839, 73.239, 73.639, 74.039, 74.839, 75.239, 75.639, 76.039, 76.439, 76.839, 77.239, 77.639, 77.839, 78.839, 79.239, 79.839, 80.039, 80.439, 80.839, 81.239, 81.439, 82.039, 82.639, 83.439, 83.639, 84.239, 84.839, 85.039, 85.439, 85.639, 86.239, 86.639, 86.839, 87.139, 87.339, 87.639, 87.939, 89.639, 89.939, 90.139, 90.439, 90.639, 90.839, 91.139, 91.539, 91.939, 92.239, 92.439, 92.639, 92.939, 93.239, 93.439, 93.639, 93.939, 94.239, 94.439, 94.839, 95.239, 95.439, 95.839, 96.039, 96.339, 96.639, 97.039, 97.339, 97.639, 98.039, 98.239, 98.439, 98.739, 99.039, 99.239, 99.539, 99.839, 100.239, 100.439, 100.739, 101.039, 101.239, 101.639, 102.039, 102.439, 102.839, 103.039, 103.539, 103.839, 104.039, 104.439, 104.639, 104.939, 105.139, 105.339, 105.539, 105.839, 106.139, 106.539, 106.839, 107.039, 107.339, 107.639, 107.839, 108.039, 108.439, 108.639, 108.839, 109.239, 109.539, 110.039, 110.239, 110.539, 110.939, 111.239, 111.639, 111.839, 112.139, 112.439, 112.639, 112.939, 113.239, 113.439, 113.639, 114.039, 114.239, 114.439, 114.639, 115.039, 115.639, 116.039, 116.439, 117.239, 117.739, 118.039, 118.439, 118.739, 118.939, 119.439, 119.639, 119.839, 120.139, 120.439, 120.639, 121.039, 121.239, 121.539, 122.039, 122.339, 122.839, 123.039, 123.339, 123.739, 124.239, 124.439, 124.639, 124.939, 125.239, 125.439, 125.739, 126.039, 126.239, 126.439, 126.839, 127.039, 127.239, 127.539, 127.739, 128.039, 128.339, 128.539, 128.839, 129.039, 129.239, 129.539, 129.839, 130.139, 130.439, 130.739, 130.939, 131.239, 131.539, 131.839, 132.039, 132.339, 132.639, 132.839, 133.239, 133.639, 133.839, 134.039, 134.239, 134.439, 134.739, 135.039, 135.439, 135.739, 136.039, 136.439, 136.739, 137.039, 137.239, 137.639, 137.939, 138.239, 138.639, 138.839, 139.139]
notes_row2 =  [13.439, 14.039, 14.639, 15.039, 15.639, 16.239, 16.839, 17.639, 18.239, 19.039, 19.839, 20.439, 21.039, 21.639, 22.239, 22.839, 23.239, 23.839, 24.839, 25.639, 26.239, 26.839, 27.639, 28.239, 28.839, 29.239, 29.639, 30.439, 31.039, 31.639, 32.039, 32.639, 33.039, 33.639, 34.039, 34.639, 35.239, 35.539, 35.939, 36.239, 36.539, 36.839, 38.439, 38.639, 39.039, 39.439, 39.739, 40.039, 40.239, 40.539, 41.039, 41.239, 41.539, 41.839, 42.239, 42.639, 42.939, 43.239, 43.539, 43.839, 44.039, 44.339, 44.539, 44.739, 45.039, 45.339, 45.639, 45.839, 46.039, 46.339, 46.639, 46.839, 47.139, 47.339, 47.639, 47.939, 48.239, 48.539, 48.839, 49.039, 49.339, 49.639, 50.039, 50.239, 50.639, 50.839, 51.339, 51.639, 51.939, 52.139, 52.439, 52.639, 52.939, 53.239, 53.439, 53.639, 54.039, 54.439, 54.839, 55.139, 55.439, 55.639, 55.939, 56.239, 56.539, 56.739, 57.039, 57.339, 57.539, 57.839, 58.039, 58.239, 58.539, 58.739, 59.039, 59.239, 59.539, 59.839, 60.139, 60.339, 60.639, 60.839, 61.239, 61.539, 61.939, 62.239, 62.439, 62.639, 63.239, 63.439, 63.739, 64.039, 64.639, 65.239, 66.039, 66.639, 67.239, 67.639, 68.039, 68.839, 69.439, 70.039, 70.439, 71.039, 71.439, 72.039, 72.439, 73.039, 73.639, 74.239, 74.639, 75.239, 75.539, 75.839, 76.139, 76.439, 76.739, 77.439, 77.639, 78.239, 78.439, 79.039, 79.239, 79.639, 79.839, 80.439, 80.639, 81.039, 81.439, 81.839, 82.039, 82.439, 82.639, 83.039, 83.239, 83.839, 84.239, 84.439, 85.239, 85.639, 86.039, 86.239, 86.539, 86.839, 87.239, 87.539, 87.839, 89.639, 89.839, 90.239, 90.639, 90.939, 91.239, 91.439, 91.739, 92.239, 92.439, 92.739, 93.039, 93.439, 93.839, 94.139, 94.439, 94.739, 95.039, 95.239, 95.539, 95.739, 95.939, 96.239, 96.539, 96.839, 97.039, 97.239, 97.539, 97.839, 98.039, 98.339, 98.539, 98.839, 99.139, 99.439, 99.739, 100.039, 100.239, 100.539, 100.839, 101.239, 101.439, 101.839, 102.039, 102.539, 102.839, 103.139, 103.339, 103.639, 103.839, 104.139, 104.439, 104.639, 104.839, 105.239, 105.639, 106.039, 106.339, 106.639, 106.839, 107.139, 107.439, 107.739, 107.939, 108.239, 108.539, 108.739, 109.039, 109.239, 109.439, 109.739, 109.939, 110.239, 110.439, 110.739, 111.039, 111.339, 111.539, 111.839, 112.039, 112.439, 112.739, 113.139, 113.439, 113.639, 113.839, 114.439, 114.839, 115.439, 116.039, 116.639, 117.039, 117.239, 117.639, 117.939, 118.439, 118.839, 119.139, 119.339, 119.639, 119.939, 120.239, 120.539, 120.739, 120.939, 121.239, 121.439, 121.739, 122.039, 122.239, 122.539, 122.739, 123.039, 123.239, 123.539, 123.839, 124.239, 124.539, 124.839, 125.239, 125.539, 125.939, 126.239, 126.439, 126.639, 127.239, 127.439, 127.839, 128.039, 128.239, 128.639, 129.039, 129.339, 129.639, 129.939, 130.239, 130.539, 130.839, 131.139, 131.339, 131.639, 131.839, 132.239, 132.539, 132.839, 133.139, 133.439, 133.739, 133.939, 134.239, 134.439, 134.639, 134.939, 135.239, 135.439, 135.639, 135.939, 136.239, 136.439, 136.639, 137.039, 137.339, 137.539, 137.839, 138.139, 138.439, 138.639, 138.939, 139.239]
notes_row3 =  [12.839, 13.639, 14.239, 14.839, 15.439, 16.039, 16.839, 17.439, 18.039, 18.639, 19.239, 19.639, 20.239, 20.639, 21.239, 22.039, 22.639, 23.439, 24.039, 24.439, 25.039, 26.039, 26.639, 27.239, 27.839, 28.439, 29.039, 29.639, 30.039, 30.639, 31.239, 31.639, 32.439, 32.839, 33.439, 34.239, 34.839, 35.439, 35.739, 36.039, 36.639, 38.539, 38.839, 39.139, 39.339, 39.639, 39.839, 40.139, 40.439, 40.639, 40.839, 41.139, 41.439, 41.639, 42.039, 42.339, 42.539, 42.839, 43.139, 43.439, 43.739, 43.939, 44.139, 44.439, 44.639, 44.839, 45.239, 45.439, 45.739, 45.939, 46.239, 46.439, 46.739, 47.039, 47.439, 47.739, 48.039, 48.439, 48.739, 49.139, 49.439, 49.639, 49.839, 50.439, 50.639, 51.039, 51.239, 51.439, 51.839, 52.239, 52.539, 52.839, 53.139, 53.539, 53.839, 54.239, 54.539, 54.839, 55.039, 55.439, 55.739, 56.039, 56.339, 56.639, 56.939, 57.139, 57.439, 57.739, 58.139, 58.439, 58.639, 58.839, 59.139, 59.439, 59.639, 59.939, 60.239, 60.539, 60.739, 61.039, 61.339, 61.639, 61.839, 62.139, 62.439, 62.839, 63.039, 63.439, 63.639, 63.939, 64.439, 65.039, 65.639, 66.239, 66.839, 67.439, 68.039, 68.439, 69.039, 69.639, 70.039, 70.839, 71.239, 71.839, 72.639, 73.239, 74.039, 74.439, 75.039, 75.439, 75.939, 76.239, 76.639, 77.039, 77.239, 77.839, 78.039, 78.439, 78.639, 79.039, 79.439, 79.639, 80.239, 80.639, 81.239, 81.639, 82.239, 82.439, 82.839, 83.239, 83.439, 83.839, 84.039, 84.439, 84.639, 85.039, 85.239, 85.839, 86.039, 86.439, 86.739, 87.039, 87.439, 87.739, 88.039, 89.739, 90.039, 90.339, 90.539, 90.839, 91.039, 91.339, 91.639, 91.839, 92.039, 92.339, 92.639, 92.839, 93.239, 93.539, 93.739, 94.039, 94.339, 94.639, 94.939, 95.139, 95.339, 95.639, 95.839, 96.039, 96.439, 96.639, 96.939, 97.139, 97.439, 97.639, 97.939, 98.239, 98.639, 98.939, 99.239, 99.639, 99.939, 100.339, 100.639, 100.839, 101.039, 101.639, 101.839, 102.239, 102.439, 102.639, 103.039, 103.439, 103.739, 104.039, 104.339, 104.739, 105.039, 105.439, 105.739, 106.039, 106.239, 106.639, 106.939, 107.239, 107.539, 107.839, 108.139, 108.339, 108.639, 108.939, 109.339, 109.639, 109.839, 110.039, 110.339, 110.639, 110.839, 111.139, 111.439, 111.739, 111.939, 112.239, 112.539, 112.839, 113.039, 113.339, 113.639, 114.039, 114.239, 114.539, 114.839, 115.239, 115.839, 116.439, 116.839, 117.039, 117.439, 117.839, 118.639, 119.039, 119.439, 119.739, 120.039, 120.339, 120.639, 120.839, 121.139, 121.339, 121.639, 121.839, 122.139, 122.439, 122.639, 122.839, 123.139, 123.439, 123.639, 123.939, 124.139, 124.439, 124.739, 125.039, 125.339, 125.639, 125.839, 126.139, 126.439, 126.839, 127.039, 127.439, 127.639, 127.939, 128.139, 128.439, 128.739, 128.939, 129.239, 129.439, 129.739, 130.039, 130.339, 130.639, 131.039, 131.239, 131.639, 131.939, 132.239, 132.439, 132.739, 133.039, 133.339, 133.539, 133.839, 134.139, 134.539, 134.839, 135.039, 135.339, 135.539, 135.839, 136.039, 136.339, 136.639, 136.939, 137.139, 137.439, 137.639, 138.039, 138.339, 138.739, 139.039, 139.239]
notes_row4 =  [12.839, 13.239, 13.639, 14.439, 15.839, 16.439, 17.039, 17.839, 18.839, 19.239, 20.039, 20.839, 21.439, 22.439, 23.039, 23.639, 24.039, 24.639, 25.439, 25.839, 26.439, 26.839, 27.239, 28.039, 28.439, 28.839, 29.439, 30.039, 30.439, 31.239, 31.839, 32.239, 32.839, 33.239, 33.839, 34.439, 35.039, 35.339, 35.839, 36.339, 36.739, 38.439, 38.839, 39.039, 39.539, 39.839, 40.039, 40.439, 40.639, 40.939, 41.339, 41.639, 41.939, 42.139, 42.639, 42.839, 43.039, 43.339, 43.639, 43.839, 44.239, 44.439, 44.739, 44.939, 45.239, 45.539, 46.039, 46.239, 46.539, 46.939, 47.439, 47.639, 47.839, 48.139, 48.439, 48.639, 48.939, 49.239, 49.439, 49.639, 50.039, 50.239, 50.439, 50.839, 51.239, 51.539, 51.739, 52.039, 52.239, 52.439, 52.739, 53.039, 53.339, 53.639, 53.839, 54.039, 54.239, 54.439, 54.739, 55.039, 55.239, 55.539, 55.839, 56.039, 56.439, 56.839, 57.039, 57.239, 57.639, 57.939, 58.239, 58.639, 58.939, 59.239, 59.639, 59.839, 60.039, 60.239, 60.439, 60.839, 61.139, 61.439, 61.839, 62.039, 62.339, 62.639, 62.839, 63.239, 63.639, 63.839, 64.239, 64.839, 65.239, 65.639, 66.439, 66.839, 67.239, 67.839, 68.439, 68.839, 69.639, 70.239, 70.639, 71.239, 71.639, 72.239, 72.839, 73.439, 73.839, 74.439, 74.839, 75.639, 76.039, 76.339, 76.539, 76.839, 77.039, 77.439, 78.039, 78.239, 78.639, 78.839, 79.439, 80.039, 80.239, 80.839, 81.039, 81.639, 81.839, 82.239, 82.839, 83.039, 83.639, 84.039, 84.639, 84.839, 85.439, 85.839, 86.439, 86.939, 87.239, 87.639, 88.039, 89.639, 90.039, 90.239, 90.739, 91.039, 91.239, 91.639, 91.839, 92.139, 92.539, 92.839, 93.139, 93.339, 93.839, 94.039, 94.239, 94.539, 94.839, 95.039, 95.439, 95.639, 95.939, 96.139, 96.439, 96.739, 97.239, 97.439, 97.739, 98.139, 98.639, 98.839, 99.039, 99.339, 99.639, 99.839, 100.139, 100.439, 100.639, 100.839, 101.239, 101.439, 101.639, 102.039, 102.439, 102.739, 102.939, 103.239, 103.439, 103.639, 103.939, 104.239, 104.539, 104.839, 105.039, 105.239, 105.439, 105.639, 105.939, 106.239, 106.439, 106.739, 107.039, 107.239, 107.639, 108.039, 108.239, 108.439, 108.839, 109.139, 109.439, 109.839, 110.139, 110.439, 110.839, 111.039, 111.239, 111.439, 111.639, 112.039, 112.339, 112.639, 113.039, 113.239, 113.539, 113.839, 114.039, 114.439, 114.739, 115.039, 115.239, 115.639, 116.239, 116.839, 117.439, 117.639, 118.039, 118.539, 118.839, 119.039, 119.239, 119.539, 119.839, 120.039, 120.439, 120.839, 121.039, 121.439, 121.639, 121.939, 122.239, 122.639, 122.939, 123.239, 123.639, 123.839, 124.039, 124.339, 124.639, 124.839, 125.139, 125.439, 125.839, 126.039, 126.339, 126.639, 126.839, 127.339, 127.639, 127.839, 128.039, 128.439, 128.639, 129.139, 129.439, 129.639, 130.039, 130.239, 130.639, 130.839, 131.039, 131.439, 131.739, 132.139, 132.439, 132.639, 132.939, 133.239, 133.439, 133.639, 134.039, 134.339, 134.839, 135.139, 135.639, 135.839, 136.139, 136.539, 136.839, 137.239, 137.439, 137.739, 138.039, 138.239, 138.539, 138.839, 139.039, 139.239]

noterectlist_row1 = []
noterectlist_row2 = []
noterectlist_row3 = []
noterectlist_row4 = []

def getrects():
    global noterectlist_row1, noterectlist_row2, noterectlist_row3, noterectlist_row4, notes_row1, notes_row2, notes_row3, notes_row4, notespeed, HEIGHT, timer
    for i in notes_row1:
        noterectlist_row1.append(pygame.Rect(310, HEIGHT-50 - (notespeed * (i - timer)), 40, 20))

    for i in notes_row2:
        noterectlist_row2.append(pygame.Rect(360, HEIGHT-50 - (notespeed * (i - timer)), 40, 20))

    for i in notes_row3:
        noterectlist_row3.append(pygame.Rect(410, HEIGHT-50 - (notespeed * (i - timer)), 40, 20))

    for i in notes_row4:
        noterectlist_row4.append(pygame.Rect(460, HEIGHT-50 - (notespeed * (i - timer)), 40, 20))

#font
font = pygame.font.SysFont(None, 40)

pygame.mixer.music.play()
#main cycle
running = True
while running:
    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_a:
                    hitsound.play()
                    time_diff = notes_row1[0] - timer
                    if abs(time_diff) <= 0.018:
                        marv_count += 1
                        ratetext = "MARV"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row1.pop(0)
                    elif abs(time_diff) <= 0.043:
                        perf_count += 1
                        ratetext = "PERF"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row1.pop(0)
                    elif abs(time_diff) <= 0.076:
                        great_count += 1
                        ratetext = "GREAT"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row1.pop(0)
                    elif abs(time_diff) <= 0.106:
                        good_count += 1
                        ratetext = "GOOD"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row1.pop(0)
                    elif abs(time_diff) <= 0.127:
                        okay_count += 1
                        ratetext = "OKAY"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row1.pop(0)
                    elif abs(time_diff) <= 0.164:
                        miss_count += 1
                        ratetext = "MISS"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row1.pop(0)
            except IndexError:
                pass

            try:
                if event.key == pygame.K_s:
                    hitsound.play()
                    time_diff = notes_row2[0] - timer
                    if abs(time_diff) <= 0.018:
                        marv_count += 1
                        ratetext = "MARV"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row2.pop(0)
                    elif abs(time_diff) <= 0.043:
                        perf_count += 1
                        ratetext = "PERF"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row2.pop(0)
                    elif abs(time_diff) <= 0.076:
                        great_count += 1
                        ratetext = "GREAT"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row2.pop(0)
                    elif abs(time_diff) <= 0.106:
                        good_count += 1
                        ratetext = "GOOD"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row2.pop(0)
                    elif abs(time_diff) <= 0.127:
                        okay_count += 1
                        ratetext = "OKAY"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row2.pop(0)
                    elif abs(time_diff) <= 0.164:
                        miss_count += 1
                        ratetext = "MISS"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row2.pop(0)
            except IndexError:
                pass

            try:
                if event.key == pygame.K_k:
                    hitsound.play()
                    time_diff = notes_row3[0] - timer
                    if abs(time_diff) <= 0.018:
                        marv_count += 1
                        ratetext = "MARV"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row3.pop(0)
                    elif abs(time_diff) <= 0.043:
                        perf_count += 1
                        ratetext = "PERF"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row3.pop(0)
                    elif abs(time_diff) <= 0.076:
                        great_count += 1
                        ratetext = "GREAT"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row3.pop(0)
                    elif abs(time_diff) <= 0.106:
                        good_count += 1
                        ratetext = "GOOD"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row3.pop(0)
                    elif abs(time_diff) <= 0.127:
                        okay_count += 1
                        ratetext = "OKAY"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row3.pop(0)
                    elif abs(time_diff) <= 0.164:
                        miss_count += 1
                        ratetext = "MISS"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row3.pop(0)
            except IndexError:
                pass

            try:
                if event.key == pygame.K_l:
                    hitsound.play()
                    time_diff = notes_row4[0] - timer
                    if abs(time_diff) <= 0.018:
                        marv_count += 1
                        ratetext = "MARV"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row4.pop(0)
                    elif abs(time_diff) <= 0.043:
                        perf_count += 1
                        ratetext = "PERF"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row4.pop(0)
                    elif abs(time_diff) <= 0.076:
                        great_count += 1
                        ratetext = "GREAT"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row4.pop(0)
                    elif abs(time_diff) <= 0.106:
                        good_count += 1
                        ratetext = "GOOD"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row4.pop(0)
                    elif abs(time_diff) <= 0.127:
                        okay_count += 1
                        ratetext = "OKAY"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row4.pop(0)
                    elif abs(time_diff) <= 0.164:
                        miss_count += 1
                        ratetext = "MISS"
                        try:
                            rating = (
                                                 marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                                         sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
                        except ZeroDivisionError:
                            rating = 0
                        notes_row4.pop(0)
            except IndexError:
                pass
    try:
        if notes_row1[0] - timer < -0.164:
            miss_count += 1
            try:
                rating = (marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
            except ZeroDivisionError:
                rating = 0
            notes_row1.pop(0)
    except IndexError:
        pass

    try:
        if notes_row2[0] - timer < -0.164:
            miss_count += 1
            try:
                rating = (
                                     marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                             sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
            except ZeroDivisionError:
                rating = 0
            notes_row2.pop(0)
    except IndexError:
        pass

    try:
        if notes_row3[0] - timer < -0.164:
            miss_count += 1
            try:
                rating = (
                                     marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                             sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
            except ZeroDivisionError:
                rating = 0
            notes_row3.pop(0)
    except IndexError:
        pass

    try:
        if notes_row4[0] - timer < -0.164:
            miss_count += 1
            try:
                rating = (
                                     marv_count + perf_count * 0.9825 + great_count * 0.65 + good_count * 0.25 + okay_count * -1 + miss_count * -0.5) / (
                             sum([marv_count, perf_count, great_count, good_count, okay_count, miss_count]))
            except ZeroDivisionError:
                rating = 0
            notes_row4.pop(0)
    except IndexError:
        pass

    pygame.draw.rect(screen, "black", baseline)

    noterectlist_row1.clear()
    noterectlist_row2.clear()
    noterectlist_row3.clear()
    noterectlist_row4.clear()

    getrects()

    pygame.draw.rect(screen, "black", (300, 0, 210, HEIGHT-50)) #задній фон

    for note in noterectlist_row1 + noterectlist_row4:
        pygame.draw.rect(screen, "white", note)

    for note in noterectlist_row2 + noterectlist_row3:
        pygame.draw.rect(screen, "#21d6e6", note)

    #pygame.draw.rect(screen, "gray", (300, (HEIGHT - 50)//1.5, 210, HEIGHT - 50))

    timerlabel = font.render(str(round(timer, 2)), True, "black")
    ratinglabel = font.render(f"rating:{round(rating*100, 2)}%", True, "black")
    ratelabel = font.render(ratetext, True, "black")
    countlabel = font.render(f"{marv_count} {perf_count} {great_count} {good_count} {okay_count} {miss_count}", True, "black")

    screen.blit(timerlabel, (WIDTH-100, HEIGHT-30))
    screen.blit(ratinglabel, (0, HEIGHT-30))
    screen.blit(ratelabel, (50, HEIGHT//2))
    screen.blit(countlabel, (WIDTH - 250, HEIGHT//2))

    pygame.display.update()
    clock.tick(FPS)
    try:
        timer +=(1/clock.get_fps())
    except ZeroDivisionError:
        pass

pygame.quit()