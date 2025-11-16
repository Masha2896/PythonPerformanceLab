import sys


def main():
    if len(sys.argv) != 3:
        print("Использование: python script.py <файл_эллипса> <файл_точек>")
        return

    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    try:
        with open(ellipse_file, 'r') as f:
            center_line = f.readline().split()
            radii_line = f.readline().split()

            x0, y0 = map(float, center_line)
            a, b = map(float, radii_line)
    except Exception as e:
        print(f"Ошибка чтения файла эллипса: {e}")
        return

    try:
        with open(points_file, 'r') as f:
            points = [tuple(map(float, line.split())) for line in f]
    except Exception as e:
        print(f"Ошибка чтения файла точек: {e}")
        return

    for x, y in points:
        value = ((x - x0) / a) ** 2 + ((y - y0) / b) ** 2

        if abs(value - 1) < 1e-10:
            print(0)
        elif value < 1:
            print(1)
        else:
            print(2)


if __name__ == "__main__":
    main()
