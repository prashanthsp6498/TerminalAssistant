import speedtest
import colorama


def test_speed():
    res = 0 
    res = speedtest.Speedtest()
    res.get_best_server()
    download = res.download()
    upload = res.upload()
    print("="*25)
    i = 0
    unit = ['', 'Kbps', 'Mbps', 'Gbps']
    download, i = human_readable(download)
    print(colorama.Fore.GREEN, 'Download: {0:.2f}'.format(download), unit[i])
    upload, i = human_readable(upload)
    print(colorama.Fore.GREEN, 'Upload: {0:.2f}'.format(upload), unit[i],
          colorama.Fore.RESET)


def human_readable(speed):
    i = 0
    while speed >= 1000:
        speed /= 1000
        i += 1
    return speed, i


test_speed()
