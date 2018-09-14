# 列表推导和可读性

def main():
    symbols = '$¢£¥€¤'
    codes = []
    # for symbol in symbols:
    #     codes.append(ord(symbol))

    codes = [ord(symbol) for symbol in symbols]
    print(codes)

if __name__ == '__main__':
    main()