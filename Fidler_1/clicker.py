import pyautogui as p
from time import sleep

def main():
    print("Collecting positions in:")
    for i in range(5)[::-1]:
        print(i)
        sleep(1)

    
    click_location = p.position()

    print('Press Ctrl-C to quit.')
    

    try:
        for i in range(1000):
            p.click(click_location, clicks=1000)
    except KeyboardInterrupt:
        print("done")
        print('\n')



if __name__ == "__main__":
    main()
