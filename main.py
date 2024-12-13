from engines.GameEngine import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Some parser')
    parser.add_argument('--type', type=str, help='type of demo to show')
    args = parser.parse_args()

    ge = GameEngine(args.type)

    ge.run()
