def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError:
        print('No existe este archivo')